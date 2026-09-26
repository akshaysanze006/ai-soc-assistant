alerts = {
    "ALT-001": {
        "alert_id": "ALT-001",
        "title": "Possible Account Compromise",
        "severity": "HIGH",
        "username": "admin",
        "source_ip": "185.10.20.50",
        "created_at": "2026-09-24T10:15:00"
    }
}

events = [
    {
        "timestamp": "2026-09-24T10:10:01",
        "event_type": "failed_login",
        "username": "admin",
        "source_ip": "185.10.20.50"
    },
    {
        "timestamp": "2026-09-24T10:10:10",
        "event_type": "failed_login",
        "username": "admin",
        "source_ip": "185.10.20.50"
    },
    {
        "timestamp": "2026-09-24T10:10:20",
        "event_type": "failed_login",
        "username": "admin",
        "source_ip": "185.10.20.50"
    },
    {
        "timestamp": "2026-09-24T10:11:01",
        "event_type": "successful_login",
        "username": "admin",
        "source_ip": "185.10.20.50"
    },
    {
        "timestamp": "2026-09-24T10:12:30",
        "event_type": "privilege_change",
        "username": "admin",
        "source_ip": "185.10.20.50"
    },
    {
        "timestamp": "2026-09-24T10:13:10",
        "event_type": "powershell_execution",
        "username": "admin",
        "source_ip": "185.10.20.50"
    }
]