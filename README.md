# Alertmanager webhook for Bale Messenger (Python Version)

Python version 3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Change on alert-webhook.py

```python
BALE_TOKEN = "*************************************"
CHAT_ID = "123456789"
```

## Alertmanager configuration example receivers

```python
receivers:
- name: bale
  webhook_configs:
  - url: http://localhost:5000/bale
    send_resolved: true
```

## One way to get the chat ID

Access ​<https://old.bale.ai/#/im> Click to specific chat to the left At the url, you can get the chat ID(Ex: <https://old.bale.ai/#/im/u123456789>, so the chatID is 123456789)

## Running

Create service  alert-webhook in /etc/systemd/system/alert-webhook.service :

```bash
# /etc/systemd/system/alert-webhook.service
[Unit]
Description=Alert Webhook
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/etc/prometheus/webhook
ExecStart=/bin/python3 alert-webhook.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl start alert-webhook.service
systemctl enable alert-webhook.service
```
