# 🛡️ SIEM Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

### 🌐 [Live Demo](https://siem-dashboard-mutf.onrender.com) — Login: `admin / admin123`

*A full-stack Security Information and Event Management system demonstrating Blue Team skills, real-time monitoring, and modern cybersecurity practices.*

</div>

---

## 📸 Preview

> Dashboard with real-time event detection, severity charts, and live alerts.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 Authentication | Login/logout with role-based access (Admin / Analyst) |
| 📊 Live Dashboard | Charts and stats auto-refresh every 10 seconds |
| 🚨 Alert System | Automated detection of HIGH and MEDIUM severity events |
| 🗄️ Persistence | SQLite database storing all security events |
| ⚡ Log Simulation | Generates realistic security events on demand |
| 🌐 Production Ready | Deployed on Render.com with Gunicorn WSGI server |

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

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.14, Flask 3.0 |
| Auth | Flask-Login, Werkzeug password hashing |
| Database | SQLite + Flask-SQLAlchemy |
| Frontend | HTML5, CSS3, JavaScript |
| Charts | Chart.js 4.4 |
| Server | Gunicorn (WSGI) |
| Deploy | Render.com |

---

## ⚙️ Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/VladimirRamirez07/siem-dashboard.git
cd siem-dashboard

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python run.py
```

Open **http://127.0.0.1:5000** and login with `admin / admin123`

---

## 📁 Project Structure

```
siem-dashboard/
│
├── app/
│   ├── __init__.py          # App factory, DB init, Login manager
│   ├── models.py            # User and LogEvent database models
│   ├── routes.py            # Dashboard API endpoints
│   ├── auth.py              # Login / logout routes
│   ├── log_generator.py     # Fake security event generator
│   │
│   ├── templates/
│   │   ├── index.html       # Main dashboard UI
│   │   └── login.html       # Login page
│   │
│   └── static/
│       ├── css/
│       │   └── style.css    # Dark theme styles
│       └── js/
│           └── dashboard.js # Real-time chart updates
│
├── requirements.txt         # Python dependencies
├── Procfile                 # Gunicorn start command
└── run.py                   # App entry point
```

## 🔗 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/` | ✅ | Main dashboard |
| GET/POST | `/login` | ❌ | Authentication |
| GET | `/logout` | ✅ | End session |
| GET | `/api/logs` | ✅ | Last 50 events |
| GET | `/api/stats` | ✅ | Event statistics |
| GET | `/api/alerts` | ✅ | HIGH/MEDIUM alerts |
| GET | `/api/generate` | ✅ | Generate 10 new events |

---

## 👤 Author

**Vladimir Ramirez** — [@VladimirRamirez07](https://github.com/VladimirRamirez07)

*Software Engineering Student | QA & Testing | Security | Backend Development*