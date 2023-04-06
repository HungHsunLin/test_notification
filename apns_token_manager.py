import jwt
import datetime

# 設定p8憑證的路徑、Key ID、Team ID和App Bundle ID
p8_file = 'path/to/p8/file'
key_id = 'ABCD1234EF'
team_id = 'ABCDEFGHIJ'
bundle_id = 'com.example.app'

def generate_token():
    # 讀取p8憑證的內容
    with open(APNS_AUTH_KEY_PATH, 'r') as f:
        private_key = f.read()
    
    # 設定JWT的header，包含alg（演算法）和kid（Key ID）
    headers = {
        'alg': 'ES256',
        'kid': key_id
    }

    # 設定JWT的payload，包含iss（發行者）、iat（發行時間）、exp（過期時間
    payload = {
        'iss': team_id,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    token = jwt.encode(
        payload, 
        private_key,
        lgorithm='ES256',
        headers=headers
    )

    return token