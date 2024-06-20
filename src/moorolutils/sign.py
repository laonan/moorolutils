import json
import hmac
import hashlib
import base64


class HMACUtil:

    def __init__(self, data, secret):
        if isinstance(data, dict):
            # should be request.body avoid this problem, not drf request.data
            data = json.dumps(data)

        data = data.replace(' ', '')
        data = data.replace('\n', '')
        data = data.replace('\t', '')
        data = data.replace('\r', '')

        if not isinstance(data, bytes):
            data = data.encode('utf-8')

        self.data = data
        self.secret = secret

    def verify_signature(self, signature):
        computed_hmac = self.sign()
        return hmac.compare_digest(computed_hmac, signature)

    def sign(self):
        digest = hmac.new(self.secret.encode('utf-8'), self.data, digestmod=hashlib.sha256).digest()
        return base64.b64encode(digest)
