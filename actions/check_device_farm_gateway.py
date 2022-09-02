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
        int : Status_code of the device_farm_gateway
    """
    try:
        device_farm_gateway = requests.get(gateway_url)
        result = device_farm_gateway.status_code
        if result != 200:
            print("Device_Farm API Error : %s" %gateway_url)
            return False, result
        return True, result
    except Exception as e:
        print('Exception : ', e)
        print(traceback.format_exc())
    finally:
        device_farm_gateway.close()
    return None

def notify_device_farm_gateway_with_slack(gateway_slack_webhook_url, msg_string):
    """Notify Slack when the device_farm_gateway server is shut down
    """
    msg = {"text": f"{msg_string}"}
    res = requests.post(gateway_slack_webhook_url, data=json.dumps(msg), headers={'Content-Type': 'application/json'})
    if res.raise_for_status()!=None:
        print(res.raise_for_status())

def main():
    DEVICE_FARM_GATEWAY_URL = os.environ.get("DEVICE_FARM_GATEWAY_URL")
    GATEWAY_SLACK_WEBHOOK_URL = os.environ.get("GATEWAY_SLACK_WEBHOOK_URL")
     
    print(DEVICE_FARM_GATEWAY_URL)
    device_farm_gateway_status, device_farm_gateway_status_code = check_device_farm_gateway_status(DEVICE_FARM_GATEWAY_URL)

    if device_farm_gateway_status:
        print("[NOTICE] device_farm_gateway is active!, STATUS_CODE : " + device_farm_gateway_status_code)
    else:
        msg_string = "*[NOTICE]* device_farm_gateway is *inactive*!\n :black_medium_small_square: STATUS_CODE : " + device_farm_gateway_status_code
        notify_device_farm_gateway_shutdown_with_slack(GATEWAY_SLACK_WEBHOOK_URL, msg_string)
    
if __name__ == '__main__':
    main()