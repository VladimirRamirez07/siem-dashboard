import random
import json
from datetime import datetime
from faker import Faker

fake = Faker()

EVENT_TYPES = ["LOGIN_SUCCESS", "LOGIN_FAILED", "FILE_ACCESS", "PORT_SCAN", "SQL_INJECTION", "BRUTE_FORCE"]
USERNAMES = ["admin", "root", "user1", "john.doe", "guest", "administrator"]
SUSPICIOUS_IPS = ["192.168.1.666", "10.0.0.99", "172.16.0.50"]

def generate_log():
    event_type = random.choice(EVENT_TYPES)
    is_suspicious = event_type in ["LOGIN_FAILED", "PORT_SCAN", "SQL_INJECTION", "BRUTE_FORCE"]
    
    log = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "source_ip": random.choice(SUSPICIOUS_IPS) if is_suspicious else fake.ipv4(),
        "username": random.choice(USERNAMES),
        "status": "FAILED" if is_suspicious else "SUCCESS",
        "severity": "HIGH" if event_type in ["SQL_INJECTION", "BRUTE_FORCE"] else
                   "MEDIUM" if event_type in ["PORT_SCAN", "LOGIN_FAILED"] else "LOW",
        "details": get_details(event_type)
    }
    return log

def get_details(event_type):
    details = {
        "LOGIN_SUCCESS": "User authenticated successfully",
        "LOGIN_FAILED": f"Failed login attempt {random.randint(1,10)} of 10",
        "FILE_ACCESS": f"Accessed file /var/log/{fake.file_name()}",
        "PORT_SCAN": f"Port scan detected on port {random.randint(1, 9999)}",
        "SQL_INJECTION": "SQL injection attempt detected in query",
        "BRUTE_FORCE": f"Brute force attack: {random.randint(10,100)} attempts/min"
    }
    return details.get(event_type, "Unknown event")

def generate_multiple_logs(count=10):
    return [generate_log() for _ in range(count)]