from flask import Flask, render_template, request
import re
import matplotlib.pyplot as plt
import mysql.connector

app = Flask(__name__)

# -------------------------
# MySQL Connection
# -------------------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakshi@123",   
    database="cyber_logs"
)

cursor = db.cursor()

# -------------------------
# Home Page
# -------------------------

@app.route("/")
def home():
    return render_template("upload.html")

# -------------------------
# Upload Route
# -------------------------

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["logfile"]
    content = file.read().decode("utf-8")

    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    ips = re.findall(ip_pattern, content)

    ip_count = {}

    # Count IP requests
    for ip in ips:
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

    suspicious = set()

    # -------------------------
    # Detect DDoS
    # -------------------------

    for ip, count in ip_count.items():
        if count > 3:
            suspicious.add(f"{ip} → Possible DDoS attack ({count} requests)")

    # -------------------------
    # Detect SQL Injection
    # -------------------------

    sql_patterns = ["' OR '1'='1", "UNION", "SELECT", "DROP", "--"]

    for pattern in sql_patterns:
        if pattern.lower() in content.lower():
            suspicious.add(f"SQL Injection pattern detected: {pattern}")

    # -------------------------
    # Save attacks to MySQL
    # -------------------------

    for item in suspicious:

        if "DDoS" in item:
            ip = item.split(" ")[0]

            cursor.execute(
                "INSERT INTO attacks (ip_address, attack_type, details) VALUES (%s,%s,%s)",
                (ip, "DDoS", item)
            )

        if "SQL" in item:
            cursor.execute(
                "INSERT INTO attacks (ip_address, attack_type, details) VALUES (%s,%s,%s)",
                ("Unknown", "SQL Injection", item)
            )

    db.commit()

    # -------------------------
    # Graph Visualization
    # -------------------------

    attack_types = {"DDoS": 0, "SQL Injection": 0}

    for item in suspicious:
        if "DDoS" in item:
            attack_types["DDoS"] += 1
        if "SQL" in item:
            attack_types["SQL Injection"] += 1

    labels = list(attack_types.keys())
    values = list(attack_types.values())

    plt.bar(labels, values)
    plt.title("Detected Cyber Attacks")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")

    plt.savefig("static/attack_graph.png")
    plt.close()

    return render_template("result.html", data=list(suspicious))

# -------------------------
# Dashboard
# -------------------------

@app.route("/dashboard")
def dashboard():

    cursor.execute("SELECT ip_address, attack_type, details, detected_at FROM attacks ORDER BY detected_at DESC")

    attacks = cursor.fetchall()

    return render_template("dashboard.html", attacks=attacks)


# -------------------------
# Run Flask
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)