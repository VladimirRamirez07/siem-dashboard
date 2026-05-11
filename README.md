# 🛡️ SIEM Dashboard

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

> **Live Demo:** https://siem-dashboard-mutf.onrender.com  
> **Credentials:** admin / admin123

A full-stack Security Information and Event Management (SIEM) system built with Python and Flask. Demonstrates Blue Team skills, real-time monitoring, and modern cybersecurity practices.

---

## 🚀 Features

- 🔐 **Authentication system** — login/logout with role-based access (admin/analyst)
- 📊 **Real-time dashboard** — live charts updating every 10 seconds
- 🚨 **Automated alerts** — HIGH and MEDIUM severity event detection
- 🗄️ **Event persistence** — SQLite database storing all security events
- ⚡ **Log simulation** — generates realistic security events on demand
- 🌐 **Production deploy** — hosted on Render.com

---

## 🔍 Detected Event Types

| Event | Severity | Description |
|-------|----------|-------------|
| Brute Force | 🔴 HIGH | Multiple failed login attempts per minute |
| SQL Injection | 🔴 HIGH | Malicious SQL detected in queries |
| Port Scan | 🟡 MEDIUM | Unauthorized port scanning detected |
| Login Failed | 🟡 MEDIUM | Failed authentication attempt |
| File Access | 🟢 LOW | File system access logged |
| Login Success | 🟢 LOW | Successful user authentication |

---

## 🛠️ Tech Stack

- **Backend:** Python 3.14, Flask 3.0, Flask-Login, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Chart.js
- **Auth:** Werkzeug password hashing, Flask-Login sessions
- **Deploy:** Render.com, Gunicorn

---

## ⚙️ Local Installation

```bash
git clone https://github.com/VladimirRamirez07/siem-dashboard.git
cd siem-dashboard
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py
```

Open **http://127.0.0.1:5000** — login with `admin / admin123`

---

## 📁 Project Structure
siem-dashboard/
├── app/
│   ├── init.py        # App factory, DB init, Login manager
│   ├── models.py          # User and LogEvent models
│   ├── routes.py          # Dashboard API endpoints
│   ├── auth.py            # Login/logout routes
│   ├── log_generator.py   # Fake security event generator
│   ├── templates/
│   │   ├── index.html     # Dashboard UI
│   │   └── login.html     # Login page
│   └── static/
│       ├── css/style.css  # Dark theme styles
│       └── js/dashboard.js # Real-time chart updates
├── requirements.txt
├── Procfile
└── run.py
---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard (requires auth) |
| `/login` | GET/POST | Authentication |
| `/logout` | GET | End session |
| `/api/logs` | GET | Last 50 events |
| `/api/stats` | GET | Event statistics |
| `/api/alerts` | GET | HIGH/MEDIUM alerts |
| `/api/generate` | GET | Generate 10 new events |