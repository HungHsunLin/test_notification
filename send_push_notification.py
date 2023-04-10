import http.client
import ssl
import apns_token_manager

device_token = '00fc13adff785122b4ad28809a3420982341241421348097878e577c991de8f0'
bundleID = 'com.notification.test'
jwt_token = apns_token_manager.generate_token

# 推播主機的URL
url = f'https://api.push.apple.com:443/3/device/{device_token}'

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

headers = {
    'apns-topic': bundleID,
    'authorization': f'bearer {jwt_token}',
    'apns-push-type': 'alert',
    'content-type': 'application/json'
}

# 創建HTTP/2連接
conn = http.client.HTTPSConnection(
    url,
    context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))

# 發送推播
conn.request(
    'POST',
    url,
    headers=headers,
    body=json_content)

# 獲取推播結果
response = conn.getresponse()
if response.status == 200:
    print('推播成功')
else:
    print('推播失敗')
