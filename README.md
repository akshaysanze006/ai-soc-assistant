# Autonomous AI SOC Assistant 🛡️

A FastAPI-based Security Operations Center (SOC) assistant powered by Gemini 2.5 Flash and Automatic Function Calling. This application autonomously investigates security alerts, synthesizes log data into structured reports mapped to MITRE ATT&CK frameworks, and provides a Human-in-the-Loop (HITL) web dashboard for authorized containment actions.

## 🚀 Key Features

* **Autonomous Log Investigation:** Automatically pulls user and IP activity logs upon receiving an alert (e.g., `ALT-001`).
* **AI-Generated Markdown Reports:** Leverages Gemini to generate rich incident reports including an Executive Summary, Chronological Timeline, and Risk Indicators.
* **Human-in-the-Loop Containment (HITL):** Web-based dashboard allowing human analysts to safely approve remediation actions like blocking an IP or locking an account with a single click.
* **Resilient Architecture:** Built-in in-memory caching and graceful 429 rate-limit handling to accommodate Gemini free-tier constraints.
* **Modern Stack:** Built on Python 3.13, FastAPI, Uvicorn, and the modern `google-genai` SDK.

## 🛠️ Tech Stack

* **Backend:** Python 3.13, FastAPI, Uvicorn, Pydantic
* **AI Integration:** Google GenAI SDK (`gemini-2.5-flash`)
* **Frontend:** HTML5, CSS (System UI), vanilla JavaScript (Fetch API), Python Markdown
* **Environment:** Virtual environments (`venv`) on Windows/PowerShell

## 📦 Installation & Setup

1.Create and activate a virtual environment:

PowerShell
python -m venv venv
.\venv\Scripts\activate

2. Install dependencies:

PowerShell
pip install -r requirements.txt

3. Configure Environment Variables:
Create a .env file in the root directory and add your Google Gemini API Key:

Code snippet
GEMINI_API_KEY=your_gemini_api_key_here

4. 🚦 Running the Application
Start the backend server:

PowerShell
python -m uvicorn main:app --reload

5. 📂 Project Structure
Plaintext
ai-soc-assistant/
│
├── main.py              # FastAPI application and routing
├── template.html        # HTML layout for the dashboard
├── requirements.txt     # Python package dependencies
├── .gitignore           # Ignored files (venv, __pycache__, .env)
├── README.md            # Project documentation
│
├── ai/
│   ├── analyst.py       # Gemini API logic, caching, and rate-limit handling
│   └── tools.py         # Mock SOC log retrieval functions (Automatic Function Calling)
│
└── data/                # Local data models or JSON log storage (if applicable)
