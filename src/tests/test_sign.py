import json
from moorolutils.sign import HMACUtil


def sign(data):
    secret = '123456'
    hmac_util = HMACUtil(data, secret)
    signature = hmac_util.sign()

    print(data)
    print(signature)
    print(hmac_util.verify_signature(signature))


def test_sign():
    data1 = {"id": 1,  "sex": 'Male', "name": "John",}
    data2 = b'{"id":"eeafa272cebfd4b22385bc4b645e762c","token":"eeafa272cebfd4b22385bc4b645e762c","line_items":[{"id":704912205188288575,"properties":{},"quantity":3,"variant_id":704912205188288575,"key":"704912205188288575:33f11f7a1ec7d93b826de33bb54de37b","discounted_price":"19.99","discounts":[],"gift_card":false,"grams":200,"line_price":"59.97","original_line_price":"59.97","original_price":"19.99","price":"19.99","product_id":788032119674292922,"sku":"example-shirt-s","taxable":true,"title":"Example T-Shirt - Small","total_discount":"0.00","vendor":"Acme","discounted_price_set":{"shop_money":{"amount":"19.99","currency_code":"USD"},"presentment_money":{"amount":"19.99","currency_code":"USD"}},"line_price_set":{"shop_money":{"amount":"59.97","currency_code":"USD"},"presentment_money":{"amount":"59.97","currency_code":"USD"}},"original_line_price_set":{"shop_money":{"amount":"59.97","currency_code":"USD"},"presentment_money":{"amount":"59.97","currency_code":"USD"}},"price_set":{"shop_money":{"amount":"19.99","currency_code":"USD"},"presentment_money":{"amount":"19.99","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.0","currency_code":"USD"},"presentment_money":{"amount":"0.0","currency_code":"USD"}}}],"note":null,"updated_at":"2024-06-21T04:20:56.903Z","created_at":"2024-06-21T04:20:56.903Z"}'
    sign(data1)
    sign(data2)

    print('+++++++++++++++++ end test_sign ++++++++++++++++++++++')


def test_verify_signature():
    secret = '123456'
    data1 = {"id": 1,  "sex": 'Male', "name": "John", }
    data2 = {"id": 1, "name": "John", "sex": 'Male', }
    data3 = {
        "id": 1,
        "sex": "Male",
        "name": "John",
    }

    hmac_util1 = HMACUtil(data1, secret)
    hmac_util2 = HMACUtil(data2, secret)
    hmac_util3 = HMACUtil(data3, secret)

    print(hmac_util1.sign() == hmac_util2.sign() == hmac_util3.sign())

    print('+++++++++++++++++ end test_verify_signature ++++++++++++++++++++++')