import os
import time
from google import genai
from google.genai import types
from google.genai.errors import APIError
from ai.tools import get_alert, get_user_activity, get_ip_activity

SYSTEM_PROMPT = """
You are an Autonomous Senior SOC Security Analyst.
Your goal is to investigate a security alert by executing available functions/tools.

Follow this exact procedure:
1. Call `get_alert` with the provided alert ID.
2. Identify the target username and source IP from the returned alert data.
3. Call `get_user_activity` and `get_ip_activity` to gather event evidence.
4. Synthesize all retrieved logs into a structured INCIDENT INVESTIGATION REPORT formatted in clear Markdown:
   - EXECUTIVE SUMMARY
   - CHRONOLOGICAL TIMELINE (with event sequence analysis)
   - RISK INDICATORS & MITRE ATT&CK MAPPINGS (e.g., T1110 Brute Force, T1078 Valid Accounts, T1059 PowerShell)
   - RECOMMENDED ACTION PLAYBOOK (Note: Actions require human analyst approval)
"""

# In-memory investigation cache: {alert_id: report_text}
INVESTIGATION_CACHE = {}

def run_autonomous_investigation(alert_id: str) -> str:
    # Return cached report immediately if available to prevent hitting rate limits
    if alert_id in INVESTIGATION_CACHE:
        return INVESTIGATION_CACHE[alert_id]

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    client = genai.Client(api_key=api_key)

    try:
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[get_alert, get_user_activity, get_ip_activity],
                temperature=0.2
            )
        )

        response = chat.send_message(f"Investigate security alert: {alert_id}")
        report_text = response.text

        # Store in cache
        INVESTIGATION_CACHE[alert_id] = report_text
        return report_text

    except APIError as e:
        if getattr(e, "code", None) == 429 or "RESOURCE_EXHAUSTED" in str(e):
            return "### ⚠️ RATE LIMIT EXCEEDED\n\nGemini API free tier limit reached (15 RPM). Please wait 10–15 seconds and refresh the browser."
        raise Exception(f"Gemini API Error: {str(e)}")