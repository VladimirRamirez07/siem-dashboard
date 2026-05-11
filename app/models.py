from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class LogEvent(db.Model):
    __tablename__ = 'log_events'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    event_type = db.Column(db.String(50), nullable=False)
    source_ip = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    details = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": self.event_type,
            "source_ip": self.source_ip,
            "username": self.username,
            "status": self.status,
            "severity": self.severity,
            "details": self.details
        }