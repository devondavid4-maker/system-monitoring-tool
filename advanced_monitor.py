import psutil
import time
import smtplib
import json
from email.mime.text import MIMEText
from datetime import datetime

# Load config
with open("config.json") as config_file:
    config = json.load(config_file)

CPU_THRESHOLD = config["cpu_threshold"]
MEMORY_THRESHOLD = config["memory_threshold"]
DISK_THRESHOLD = config["disk_threshold"]
CHECK_INTERVAL = config["check_interval"]

EMAIL_CONFIG = config["email"]

def log(message):
    timestamp = datetime.now()
    with open("monitor.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")

def send_email(subject, message):
    if not EMAIL_CONFIG["enabled"]:
        return

    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_CONFIG["sender"]
        msg["To"] = EMAIL_CONFIG["receiver"]

        server = smtplib.SMTP(
            EMAIL_CONFIG["smtp_server"],
            EMAIL_CONFIG["smtp_port"]
        )
        server.starttls()
        server.login(
            EMAIL_CONFIG["sender"],
            EMAIL_CONFIG["password"]
        )
        server.sendmail(
            EMAIL_CONFIG["sender"],
            EMAIL_CONFIG["receiver"],
            msg.as_string()
        )
        server.quit()

    except Exception as e:
        print(f"Email failed: {e}")

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alert = f"HIGH CPU: {cpu}%"
        print(alert)
        log(alert)
        send_email("CPU Alert", alert)

def check_memory():
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        alert = f"HIGH MEMORY: {memory}%"
        print(alert)
        log(alert)
        send_email("Memory Alert", alert)

def check_disk():
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        alert = f"HIGH DISK: {disk}%"
        print(alert)
        log(alert)
        send_email("Disk Alert", alert)

def monitor():
    log("Monitoring started")
    print("Monitoring started...")
    while True:
        check_cpu()
        check_memory()
        check_disk()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
