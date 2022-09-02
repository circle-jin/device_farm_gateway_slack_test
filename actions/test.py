import requests
import json
import os

def check_gateway_status(gateway_url):
    """Returns the current server status of the device_farm_gateway.
    Args:
        gateway_url (string): url address of device_farm_gateway
    Returns:
        bool: Returns True when the server is open, False when the server is closed
    """
    try:
        device_farm_gateway = requests.get(gateway_url)
        if device_farm_gateway.status_code != 200:
            print("Device_Farm API Error : %s" %gateway_url)
            return False
        return True
    except Exception as e:
        print('Exception : ', e)
        print(traceback.format_exc())
    finally:
        device_farm_gateway.close()

def notify_to_slack():
    """_summary_
    """    

    webhook_url = "https://hooks.slack.com/services/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"
    msg_string = "[NOTICE] device_farm_gateway의 서버가 종료되었습니다. "
    msg = {"text": f"{msg_string}"}
    requests.post(webhook_url, data=json.dumps(msg), headers={'Content-Type': 'application/json'})

def main():
    GATEWAY_URL = os.environ.get("GATEWAY_URL")
    print(GATEWAY_URL)
    gateway_status = check_gateway_status(GATEWAY_URL)

    if gateway_status:
        print("device_farm_gateway 서버가 정상 작동 중입니다.")
    else:
        notify_to_slack()
    
if __name__ == '__main__':
    main()