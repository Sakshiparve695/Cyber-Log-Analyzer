# 🔐 Cyber Log Analyzer System

A smart **cybersecurity monitoring system** that analyzes server log files to detect potential security threats such as **SQL Injection attacks** and **Distributed Denial of Service (DDoS) attacks**.

The system processes uploaded log files, identifies suspicious patterns, stores detected attacks in a **MySQL database**, and visualizes attack statistics using graphs.

---

# 🚀 Features

- Upload and analyze server log files
- Detect **SQL Injection patterns** in requests
- Detect potential **DDoS attacks** based on request frequency
- Store detected attacks in **MySQL database**
- Visualize attack statistics using **Matplotlib graphs**
- View attack history in a **Live Security Dashboard**

---

# 🛠 Tech Stack

- Python  
- Flask  
- MySQL  
- Matplotlib  
- HTML  
- CSS  

---

# 🧠 Detection Logic

The system uses **pattern matching and request frequency analysis** to identify suspicious activities.

### SQL Injection Detection

The system scans log entries for common SQL injection patterns such as:

```
' OR '1'='1
UNION
SELECT
DROP
--
```

### DDoS Detection

Steps:

1. Extract IP addresses from log entries  
2. Count number of requests per IP  
3. If requests exceed threshold → mark as potential **DDoS attack**

---

# 📊 Attack Visualization

Detected attacks are visualized using graphs.

The visualization shows:

- Number of SQL Injection attempts
- Number of DDoS attacks detected

Example output:

```
Attack Type      Count
----------------------
DDoS             1
SQL Injection    1
```

---

# 📷 Live Attack Dashboard

The system includes a **Flask dashboard** that displays all detected attacks stored in the database.

Displayed information:

- IP Address  
- Attack Type  
- Attack Details  
- Detection Timestamp  

This provides a **basic security monitoring interface**.

---

# 🗂 Project Structure

```
Cyber-Log-Analyzer
│
├── app.py
├── log.txt
├── requirements.txt
│
├── static
│   ├── style.css
│   └── attack_graph.png
│
├── templates
│   ├── upload.html
│   ├── result.html
│   └── dashboard.html
│
└── database
    └── schema.sql
```

---

# ⚙️ How to Run the Project

1. Install required libraries

```
pip install flask
pip install mysql-connector-python
pip install matplotlib
```

2. Run the application

```
python app.py
```

3. Open the browser

```
http://127.0.0.1:5000
```

Upload a log file to start analyzing threats.

---

# 🔮 Future Improvements

- Detect **Brute Force login attacks**
- Real-time log monitoring
- Email alerts for detected threats
- Advanced threat visualization dashboard
- Integration with SIEM systems

---

# 👩‍💻 Author

**Sakshi Parve**
