
from datetime import datetime, timedelta
import storage

def correlate():
    incidents = storage.load_incidents()
    correlated = []

    now = datetime.now()
    recent = [
        inc for inc in incidents
        if datetime.strptime(inc["time"], "%Y-%m-%d %H:%M:%S") > now - timedelta(minutes=5)
    ]

    if len(recent) > 1:
        correlated.append({
            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "type": "Multiple Attacks",
            "severity": "High",
            "description": f"{len(recent)} incidents detected in last 5 minutes"
        })

    return correlated
