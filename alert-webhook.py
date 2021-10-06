import json
import os
from flask import Flask, request
import requests

app = Flask(__name__)

BALE_TOKEN = "*************************************"
CHAT_ID = "************"

class Bale:
    token = os.environ.get("BALE_TOKEN", BALE_TOKEN)
    IDs = [CHAT_ID]

def send_bale_alert(bale_ids, message):
    for bale_id in bale_ids:
        send_user_bale_alert(bale_id, message)

def send_user_bale_alert(bale_id, message):
    try:
        url = "https://tapi.bale.ai/bot{token}/sendMessage".format(token=Bale.token)
        payload = f"chat_id={bale_id}&text={message}&parse_mode=Markdown".replace(" ", "%20").replace("\n", "%0A")
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        requests.request("POST", url, data=payload, headers=headers)
    except Exception as e:
        print(e)

@app.route('/bale', methods=['POST'])
def bale():
    content = json.loads(request.get_data())
    alerts = content.get('alerts')
    if alerts:
       for alert in alerts:
           message = "*Status:* " + alert['status'] + "\n"
           labels = alert.get('labels')
           if labels:
               for key,value in labels.items():
                   message += f'*{key}:* {value}\n'
           annotations = alert.get('annotations')
           if annotations:
               for key,value in annotations.items():
                   message += f'*{key}:* {value}\n'
           if alert['status'] == "resolved":
               date = alert['endsAt']
               message += "*Resolved:* " + date
           elif alert['status'] == "firing":
               date = alert['startsAt']
               message += "*Started:* " + date
           send_bale_alert(Bale.IDs, message)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json', "last_status": 0}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)