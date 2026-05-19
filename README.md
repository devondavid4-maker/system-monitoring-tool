System Monitoring Tool

Python-based monitoring system designed to simulate real-world production monitoring and incident response.

Features

CPU, memory, and disk monitoring

Threshold-based alerting

Email notifications

Logging and incident tracking

Configurable settings using JSON

Runs as a background service on Windows

Tech Stack

Python

psutil

SMTP

JSON configuration

Purpose

Built to demonstrate proactive monitoring, automation, and support engineering concepts in production-like environments.

## How It Works
The script continuously monitors system resources and compares them against configurable thresholds.  
If thresholds are exceeded:
- Alerts are triggered
- Events are logged
- Optional email notifications are sent

This simulates real-world monitoring and incident response workflows.
