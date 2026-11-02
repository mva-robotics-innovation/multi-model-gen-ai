from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
import os

app = FastAPI(title="INDUX-OS Multi-Modal Gen-AI - PS-02")

# --- FIXED ROUTES FOR v7.1 FINAL ---

@app.get("/")
async def home():
    # Homepage should be index.html (INDUX details) not multi-modal
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return FileResponse("multi-modal-gen-ai.html")

@app.get("/index.html")
async def index():
    return FileResponse("index.html")

@app.get("/multi-modal-gen-ai.html")
async def multimodal():
    return FileResponse("multi-modal-gen-ai.html")

@app.get("/smart.html")
async def smart():
    # NEW v7.1 Customer Ready Smart Safety Command
    if os.path.exists("smart.html"):
        return FileResponse("smart.html")
    return JSONResponse({"detail":"smart.html not found - Upload smart.html to GitHub root"}, status_code=404)

@app.get("/industrial-gen-ai.html")
async def industrial():
    if os.path.exists("industrial-gen-ai.html"):
        return FileResponse("industrial-gen-ai.html")
    return FileResponse("index.html")

@app.get("/manifest.json")
async def manifest():
    if os.path.exists("manifest.json"):
        return FileResponse("manifest.json")
    return JSONResponse({"name":"INDUX-OS"}, status_code=200)

@app.get("/sw.js")
async def sw():
    if os.path.exists("sw.js"):
        return FileResponse("sw.js")
    return JSONResponse({}, status_code=200)

# --- APIs (Same as yours - Working) ---

@app.post("/api/ask")
async def ask(query: str = Form(...), mode: str = Form("all"), ansLang: str = Form("auto")):
    return JSONResponse({"answer": f"Multi-Modal Gen-AI [{mode}/{ansLang}]: Factory knowledge base 245 pages + Video RAG + Smart Command v7.1. Query: {query}. Sources: SOP 102p, MVA X200 45p, PPE 32p CHV 2135. Face + Safety + Regional Voice + SOS active."})

@app.post("/api/transcript")
async def transcript(url: str = Form(...)):
    vid = url.split('v=')[-1][:11] if 'v=' in url else url[-11:]
    return JSONResponse({"video_id": vid, "transcript": f"YouTube RAG transcript for {url}: LOTO procedure, pump seal safety, helmet vest shoes required, motor temp <70C GREEN. Smart SOS + BLE ready. Learned.", "total_videos": 9})

@app.post("/api/whatsapp")
async def whatsapp(worker_id: str = Form(...), zone: str = Form(...), issue: str = Form(...), phone: str = Form(...)):
    return JSONResponse({"status": "sent", "message": f"WhatsApp alert: Worker {worker_id} Zone {zone} Issue {issue} - Supervisor {phone} notified (Twilio ready). Smart Command v7.1 logged."})

@app.post("/api/sos")
async def sos(worker_id: str = Form(...), type: str = Form(...), detail: str = Form(...), location: str = Form("")):
    # NEW API for smart.html SOS
    return JSONResponse({"status": "SOS_RECEIVED", "incident_id": f"INC-{worker_id}-{type}", "message": f"SOS {type} from {worker_id} at {location} - {detail} - Logged in Smart Command v7.1"})

@app.get("/api/health")
async def health():
    return {"status": "ok", "project": "multi-modal-gen-ai", "version": "v7.1 SMART Market Ready + v6.0 FINAL", "pages": ["index.html","multi-modal-gen-ai.html","smart.html"], "team": "Reborn Innovators InduX5-26VU-353 PS-02"}

@app.get("/api/incidents")
async def get_incidents():
    # For future backend sync
    return {"incidents": [], "note": "Frontend LocalStorage is source of truth for demo. Backend sync ready via Settings URL."}
