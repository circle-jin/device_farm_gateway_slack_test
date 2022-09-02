import requests
import json
import os
import traceback

def check_device_farm_gateway_status(gateway_url):
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

def notify_device_farm_gateway_shutdown_with_slack():
    """Notify Slack when the device_farm_gateway server is shut down
    """
    print("tttt")
    webhook_url = "https://hooks.slack.com/services/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"
    msg_string = "[NOTICE] device_farm_gateway 서버가 종료되었습니다. "
    msg = {"text": f"{msg_string}"}
    requests.post(webhook_url, data=json.dumps(msg), headers={'Content-Type': 'application/json'})
    print("END")

def main():
    DEVICE_FARM_GATEWAY_URL = os.environ.get("DEVICE_FARM_GATEWAY_URL")
    print(DEVICE_FARM_GATEWAY_URL)
    device_farm_gateway_status = check_device_farm_gateway_status(DEVICE_FARM_GATEWAY_URL)

    if device_farm_gateway_status:
        print("device_farm_gateway 서버가 정상 작동 중입니다.")
    else:
        notify_device_farm_gateway_shutdown_with_slack()
    
if __name__ == '__main__':
    main()