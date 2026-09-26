from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import markdown
from pydantic import BaseModel
from ai.analyst import run_autonomous_investigation

app = FastAPI(title="Autonomous SOC Assistant", version="2.0.0")

containment_actions = []

class ContainmentRequest(BaseModel):
    alert_id: str
    action_type: str
    target: str
    approved_by: str

@app.get("/")
def home():
    return {"message": "Autonomous SOC Assistant Engine is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/alerts/{alert_id}/investigate")
def investigate(alert_id: str):
    try:
        report = run_autonomous_investigation(alert_id)
        return {
            "alert_id": alert_id,
            "status": "INVESTIGATION_COMPLETE",
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/alerts/{alert_id}/report", response_class=HTMLResponse)
def get_report_html(alert_id: str):
    try:
        raw_markdown = run_autonomous_investigation(alert_id)
        html_content = markdown.markdown(raw_markdown, extensions=['tables', 'fenced_code'])
        
        # Read HTML template directly from file to prevent string parsing issues
        template_path = Path("template.html")
        if not template_path.exists():
            raise HTTPException(status_code=500, detail="template.html not found")
            
        template_str = template_path.read_text(encoding="utf-8")
        
        # Inject dynamic values cleanly
        rendered_html = template_str.replace("{{ alert_id }}", alert_id).replace("{{ report_body }}", html_content)
        return rendered_html
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/actions/execute")
def execute_containment(req: ContainmentRequest):
    record = {
        "action": req.action_type,
        "target": req.target,
        "alert_id": req.alert_id,
        "approved_by": req.approved_by,
        "status": "SUCCESS"
    }
    containment_actions.append(record)
    return {"status": "SUCCESS", "message": f"{req.action_type} executed for target {req.target} by {req.approved_by}."}

@app.get("/actions/audit")
def get_action_audit():
    return {"audit_log": containment_actions}