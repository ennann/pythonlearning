import hashlib
import base64
import hmac
import requests


def gen_sign(timestamp, secret):
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign

url = "https://open.feishu.cn/open-apis/meeting_room/alert/detail?room_id=omm_7c238e13452482382f1280c870aa5888"
mr_url = "https://open.feishu.cn/open-apis/vc/v1/room_configs/set"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}

access_token =

response = requests.get(url, headers=headers, token=, conten)
print(response.text)