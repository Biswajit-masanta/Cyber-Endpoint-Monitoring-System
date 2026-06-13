import requests

def send_report(data):
    return requests.post(
        "http://localhost:8000/report",
        json=data
    )