Alertmanager webhook for Bale Messenger (Python Version)

Python version 3

INSTALL
pip install -r requirements.txt
Change on alert-webhook.py
BALE_TOKEN
CHAT_ID

Alertmanager configuration example
receivers:
- name: bale
  webhook_configs:
  - url: http://localhost:5000/bale
    send_resolved: true

One way to get the chat ID
Access https://old.bale.ai/#/im
Click to specific chat to the left
At the url, you can get the chat ID(Ex: https://old.bale.ai/#/im/u123456789, so the chatID is 123456789)
Running
python alert-webhook.py
