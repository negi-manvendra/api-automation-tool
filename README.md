# 🚀 API Automation Tool

A **production-ready DevOps-style automation tool** built using **Python + Linux**, designed to interact with APIs, process data, handle failures, and log all activity.

---

## 📌 Project Overview

This project demonstrates how to build a **real-world API automation system** from scratch.

It performs:

* 🌐 API requests (HTTP GET)
* 📦 JSON data parsing
* ⚙️ Data processing
* 🧾 Logging system
* ❌ Error handling
* ⏰ Automation-ready (cron compatible)

---

## 🧠 Why This Project Matters

In real DevOps environments, APIs are used for:

* CI/CD automation
* Cloud operations
* Monitoring systems
* Infrastructure management

This project simulates those real-world workflows.

---

## 🛠️ Tech Stack

* **Linux**
* **Python 3**
* **Requests library**
* **Git (version control)**

---

## 📁 Project Structure

```
api-automation-tool/
│
├── scripts/
│   └── api_tool.py        # Main automation script
│
├── config/
│   └── config.json       # API configuration
│
├── logs/
│   └── api.log           # Execution logs
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/api-automation-tool.git
cd api-automation-tool
```

---

### 2️⃣ Install Dependencies

```bash
pip install requests
```

---

### 3️⃣ Configure API

Edit:

```
config/config.json
```

Example:

```json
{
  "api_url": "https://jsonplaceholder.typicode.com/posts/1",
  "timeout": 5,
  "log_file": "../logs/api.log"
}
```

---

## ▶️ Running the Tool

```bash
cd scripts
python3 api_tool.py
```

OR (if executable):

```bash
./api_tool.py
```

---

## 🧪 Expected Output

### Terminal:

```
✅ API call successful. Check logs for details.
```

---

### Logs (`logs/api.log`):

```
INFO - Starting API automation tool
INFO - Title: ...
INFO - Body: ...
INFO - Execution finished
```

---

## ⚠️ Error Handling

The tool safely handles:

* ⛔ Network failures
* ⏱️ Timeouts
* ❌ Invalid JSON
* 🔴 Bad status codes

Errors are logged instead of crashing the script.

---

## 🧾 Logging System

All activity is recorded in:

```
logs/api.log
```

This ensures:

* Debugging capability
* Monitoring support
* Production reliability

---

## ⏰ Automation (Cron Job)

You can schedule the script using cron:

```bash
crontab -e
```

Example (run every 5 minutes):

```bash
*/5 * * * * /usr/bin/python3 /path/to/api_tool.py
```

---

## 🔁 Workflow

```
Load Config → API Request → Validate Response → Parse JSON → Log Output
```

---

## 🧩 Real DevOps Use Cases

This tool can be adapted for:

* 🔄 CI/CD pipeline triggers
* ☁️ Cloud API automation
* 📊 Monitoring & alerting
* 🧪 Health checks

---

## 📚 Key Concepts Covered

* API fundamentals
* HTTP requests & responses
* JSON parsing
* Error handling (try/except)
* Logging system
* Automation with cron
* Git version control

---

## 🚀 Future Improvements

* Add POST/PUT support
* Retry mechanism
* API authentication (tokens)
* Multiple endpoint support
* Docker containerization

---

## 👨‍💻 Author

**Manvendra Negi**

---

## ⭐ Final Note

This project is designed to help you:

* Think like a DevOps engineer
* Build production-ready automation
* Understand APIs deeply

---

👉 If this helped you, consider starring ⭐ the repo!
