# 🛡️ Cyber Endpoint Monitoring System

A lightweight Endpoint Monitoring System built with **Python**, **FastAPI**, **SQLite**, and **HTML/CSS**.

This project collects system information from multiple Windows machines and displays it on a centralized monitoring dashboard in real time.

---

# Features

* ✅ Multi-device monitoring
* ✅ Windows monitoring agent
* ✅ Real-time dashboard
* ✅ Online / Offline detection
* ✅ Last Seen tracking
* ✅ CPU Usage monitoring
* ✅ RAM Usage monitoring
* ✅ Disk Usage monitoring
* ✅ SQLite database
* ✅ Configurable server via JSON configuration
* ✅ Standalone Windows Agent (.exe)

---

# Technologies Used

* Python
* FastAPI
* SQLite
* Jinja2
* HTML5
* CSS3
* Requests
* Psutil
* PyInstaller

---

# Project Structure

```
Cyber-Endpoint-Monitoring-System
│
├── dashboard/
│   ├── index.html
│   └── static/
│
├── modules/
│   ├── db_operations.py
│   ├── sender.py
│   ├── sys_info.py
│   └── resource_info.py
│
├── server.py
├── agent.py
├── config.json.example
├── monitoring.db
├── requirements.txt
└── README.md
```

---

# How It Works

1. The Windows Agent collects:

* Hostname
* Operating System
* CPU Usage
* Memory Usage
* Disk Usage

2. The agent sends the information to the FastAPI server every few seconds.

3. The server stores the latest information inside SQLite.

4. The dashboard displays all connected devices with their current status.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Biswajit-masanta/Cyber-Endpoint-Monitoring-System.git

cd Cyber-Endpoint-Monitoring-System
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure the agent

Rename

```
config.json.example
```

to

```
config.json
```

Then edit the server IP address.

Example:

```json
{
    "server": "http://YOUR_SERVER_IP:8000/report",
    "interval": 10
}
```

---

## Start the server

```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

Open the dashboard:

```
http://localhost:8000/dashboard
```

---

## Run the Agent

```bash
python agent.py
```

or build a standalone executable using:

```bash
pyinstaller --onefile agent.py
```

---

# Screenshots

Add screenshots inside a folder named `screenshots`.

Example:

```
screenshots/dashboard.png
screenshots/multiple-devices.png
```

---

# Future Improvements

* Live dashboard auto refresh
* Authentication
* Device search
* Sorting and filtering
* Historical CPU/RAM graphs
* Windows Service support
* Secure HTTPS communication
* Email alerts
* Process monitoring
* Installed software inventory

---

# Educational Purpose

This project was developed for learning system monitoring, networking, backend development, and cybersecurity concepts. It is intended for educational and laboratory environments.

---

# Author

**Biswajit Masanta**

Cybersecurity Student • Python Developer • Backend Enthusiast
