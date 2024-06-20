from moorolutils.sign import HMACUtil


def test_sign():
    data = {"id": 1, "name": "John"}
    secret = '123456'
    hmac_util = HMACUtil(data, secret)
    signature = hmac_util.sign()
    print(signature)
    print(hmac_util.verify_signature(signature))
    assert signature == b'fCeeLrr5pnzl9JOSUSSA4zPHjaSKkiFokMMwi3L1+tg='


test_sign()
