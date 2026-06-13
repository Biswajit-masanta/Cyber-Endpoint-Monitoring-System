from fastapi import FastAPI, Request
from datetime import datetime
from fastapi.templating import Jinja2Templates
from modules.db_operations import save_device, get_devices
from fastapi.staticfiles import StaticFiles
from datetime import timedelta

app = FastAPI()
templates = Jinja2Templates(directory="dashboard")

@app.get("/")
def home():
    return {
        "message": "Welcome to the monitoring server!"
    }


app.mount("/static", StaticFiles(directory="dashboard/static"), name="static")


@app.post("/report")
def report(data: dict):

    data["timestamp"] = str(datetime.now())

    save_device(data)

    return {
        "message": "Data received successfully!"
    }


@app.get("/devices")
def devices():

    return get_devices()

@app.get("/dashboard")

@app.get("/dashboard")
def dashboard(request: Request):

    devices = get_devices()
    updated_devices = []
    online_count = 0
    offline_count = 0
    total_cpu = 0
    total_devices = len(devices)

    for device in devices:
            
            
            timestamp = device[6]
            total_cpu += device[3]
    
            old_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
            curr_time = datetime.now()

            time_diff = curr_time - old_time

            seconds = time_diff.total_seconds()

            if seconds < 60:
                 last_seen = f"{int(seconds)} seconds ago"
            elif seconds < 3600:
                last_seen = f"{int(seconds // 60)} minutes ago"
            else:
                last_seen = f"{int(seconds // 3600)} hours ago"

            if seconds < 30:
                status = "Online"
                online_count += 1
            else:
                status = "Offline"
                offline_count += 1

            updated_devices.append({
                "hostname": device[0],
                "os": device[1],
                "version": device[2],
                "cpu": device[3],
                "memory": device[4],
                "disk": device[5],
                "last_seen": last_seen,
                "status": status
            })
    
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "devices": updated_devices,
        "online_count": online_count,
        "offline_count": offline_count,
        "avg_cpu": total_cpu / total_devices if total_devices > 0 else 0
    })
