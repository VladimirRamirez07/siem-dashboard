from flask import Blueprint, jsonify, render_template
from .models import db, LogEvent
from .log_generator import generate_multiple_logs
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/logs')
def get_logs():
    logs = LogEvent.query.order_by(LogEvent.timestamp.desc()).limit(50).all()
    return jsonify([log.to_dict() for log in logs])

@main.route('/api/generate')
def generate_logs():
    new_logs = generate_multiple_logs(10)
    for log_data in new_logs:
        log = LogEvent(
            timestamp=datetime.fromisoformat(log_data['timestamp']),
            event_type=log_data['event_type'],
            source_ip=log_data['source_ip'],
            username=log_data['username'],
            status=log_data['status'],
            severity=log_data['severity'],
            details=log_data['details']
        )
        db.session.add(log)
    db.session.commit()
    return jsonify({"message": f"Generated 10 new logs", "status": "success"})

@main.route('/api/stats')
def get_stats():
    total = LogEvent.query.count()
    high = LogEvent.query.filter_by(severity='HIGH').count()
    medium = LogEvent.query.filter_by(severity='MEDIUM').count()
    low = LogEvent.query.filter_by(severity='LOW').count()
    failed = LogEvent.query.filter_by(status='FAILED').count()

    event_types = db.session.query(
        LogEvent.event_type,
        db.func.count(LogEvent.event_type)
    ).group_by(LogEvent.event_type).all()

    return jsonify({
        "total": total,
        "severity": {"HIGH": high, "MEDIUM": medium, "LOW": low},
        "failed_events": failed,
        "event_types": {e[0]: e[1] for e in event_types}
    })

@main.route('/api/alerts')
def get_alerts():
    alerts = LogEvent.query.filter(
        LogEvent.severity.in_(['HIGH', 'MEDIUM'])
    ).order_by(LogEvent.timestamp.desc()).limit(20).all()
    return jsonify([log.to_dict() for log in alerts])