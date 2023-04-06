from hyper import HTTP20Connection
import json
import apns_token_manager

push_host = 'api.push.apple.com'
push_port = 443
device_token = 'eabeae54-14a8-11e5-b60b-1697f925ec7b'
path = '/3/device/{}'.format(device_token)
bundleID = 'com.notification.test'
jwt_token = apns_token_manager.generate_token

# 推播內容
payload = {
    'aps': {
        'alert': {
            'title': '測試推播標題',
            'subtitle': '測試推播副標題文字',
            'body': '推播內容文字'
        }
    }
}
payload_data = json.dumps(payload).encode('utf-8')

headers = {
    'apns-topic': path,
    'authorization': 'bearer {}'.format(jwt_token),
    'content-type': 'application/json'
}

conn = HTTP20Connection(push_host, port=push_port, secure=True)
conn.request('POST',
             path,
             body=payload_data,
             headers=headers)

resp = conn.get_response()

print(resp.status)
print(resp.read())

