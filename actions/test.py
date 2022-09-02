print("@@@@@@@@@@@@@@@@@@@@@")

# requests 와 json 을 활용하여 slack bot 조작하기
import requests
import json

# 메시지를 보내는 부분. 함수 안 argument 순서 :
# token : Slack Bot의 토큰
# channel : 메시지를 보낼 채널 #stock_notice
# text : Slack Bot 이 보낼 텍스트 메시지. 마크다운 형식이 지원된다.
# attachments : 첨부파일. 텍스트 이외에 이미지등을 첨부할 수 있다.


def check_gateway_status(self, gateway_url):
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
    webhook_url = "https://hooks.slack.com/services/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"
    msg_string = "[NOTICE] device_farm_gateway의 서버가 종료되었습니다. "
    msg = {"text": f"{msg_string}"}
    requests.post(webhook_url, data=json.dumps(msg), headers={'Content-Type': 'application/json'})


notify_to_slack()


def main():
    GATEWAY_URL = os.environ.get("GATEWAY_URL")
    print(GATEWAY_URL)
    
if __name__ == '__main__':
    main()