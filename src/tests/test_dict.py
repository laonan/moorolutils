from moorolutils.sign import HMACUtil


def test_dict():
    data = {
        'name':      'John',
        'id': 1
    }

    s = HMACUtil.sort_dict_string(data)
    print('ordered data:', s)
    print('+++++++++++++++++ end test_dict ++++++++++++++++++++++')
