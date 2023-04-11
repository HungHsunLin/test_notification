import http.client
import ssl
import json
import apns_token_manager


def generate_send_notification_connection():
    device_token = '00fc13adff785122b4ad28809a3420982341241421348097878e577c991de8f0'
    bundleID = 'com.notification.test'
    jwt_token = apns_token_manager.generate_token()

    # 推播主機的URL
    host = 'api.sandbox.push.apple.com'
    path = f'/3/device/DEVICE_TOKEN{device_token}'

    # 推播內容
    json_content = {
        'aps': {
            'alert': {
                'title': '測試推播標題',
                'subtitle': '測試推播副標題文字',
                'body': '推播內容文字'
            }
        }
    }
    json_data = json.dumps(json_content).encode('utf-8')

    headers = {
        'host': host,
        'apns-topic': bundleID,
        'authorization': f'bearer {jwt_token}',
        'apns-push-type': 'alert',
        'content-type': 'application/json'
    }

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.minimum_version = ssl.TLSVersion.TLSv1_2  # 使用 TLS 1.2 或更高版本

    # 創建HTTP/2連接
    conn = http.client.HTTPSConnection(
        host,
        context=context
    )

    # 設定HTTP/2.0的協定
    conn._http_vsn = 2
    conn._http_vsn_str = 'HTTP/2.0'

    # 發送推播
    conn.request(
        'POST',
        path,
        headers=headers,
        body=json_data)

    return conn


connection = generate_send_notification_connection()

# 獲取推播結果
response = connection.getresponse()

if response.status == 200:
    print('推播成功')
else:
    print('推播失敗')

# 關閉HTTP/2連接
connection.close()
