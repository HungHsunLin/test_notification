import jwt
import datetime

# 設定p8憑證的路徑、Key ID、Team ID和App Bundle ID
private_key_file = '/Users/tony760815/Desktop/test_notification/private_key.pem'
key_id = 'ABCD1234EF'
team_id = 'ABCDEFGHIJ'


def generate_token():
    # 讀取p8憑證的內容
    with open(private_key_file, 'r') as f:
        private_key = f.read()

    # 設定JWT的header，包含alg（演算ß法）和kid（Key ID）
    headers = {
        'alg': 'ES256',
        'kid': key_id,
        'typ': 'JWT'
    }

    # 設定JWT的payload，包含iss（發行者）、iat（發行時間）、exp（過期時間）
    payload = {
        'iss': team_id,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    token = jwt.encode(
        payload,
        private_key,
        algorithm='ES256',
        headers=headers
    )

    return token


print(generate_token())
