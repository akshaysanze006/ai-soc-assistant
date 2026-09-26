from data.alerts import alerts, events

# --- 1. Python Tool Functions ---
def get_alert(alert_id: str):
    return alerts.get(alert_id)

def get_user_activity(username: str):
    return [e for e in events if e["username"] == username]

def get_ip_activity(source_ip: str):
    return [e for e in events if e["source_ip"] == source_ip]

# Map tool names to Python functions
TOOL_MAP = {
    "get_alert": get_alert,
    "get_user_activity": get_user_activity,
    "get_ip_activity": get_ip_activity
}

# --- 2. OpenAI Function Schemas ---
SOC_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_alert",
            "description": "Fetch security alert metadata by alert ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "alert_id": {"type": "string", "description": "Alert ID (e.g., ALT-001)"}
                },
                "required": ["alert_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_activity",
            "description": "Retrieve all logged telemetry events for a given user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Username to query"}
                },
                "required": ["username"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ip_activity",
            "description": "Retrieve all logged telemetry events for a given source IP.",
            "parameters": {
                "type": "object",
                "properties": {
                    "source_ip": {"type": "string", "description": "Source IP address to query"}
                },
                "required": ["source_ip"]
            }
        }
    }
]