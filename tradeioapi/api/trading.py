import hashlib
import hmac
import time

import requests


def order_post():
    pass

def order_delete():
    pass

def open_orders_get():
    pass

def closed_orders_get():
    pass

def account_get(key, secret):
    params = dict(
        ts="%s000" % int(time.time())
    )
    headers = dict()

    prepared_request = requests.Request(
        "GET",
        "https://api.exchange.trade.io/api/v1/account",
        params=params,
        headers=headers).prepare()

    _, qs = prepared_request.path_url.split("?")
    sign = hmac.new(
        bytes(secret, 'utf-8'),
        bytes("?" + qs, 'utf-8'),
        digestmod=hashlib.sha512
    )
    prepared_request.headers["Sign"] = sign.hexdigest().upper()
    prepared_request.headers["Key"] = key

    with requests.Session() as session:
        response = session.send(prepared_request)

    return response

#
# import requests
# import hmac
# import hashlib
#
#
# request = requests.Request(
#     'POST', 'https://poloniex.com/tradingApi',
#     data=payload, headers=headers)
# prepped = request.prepare()
# signature = hmac.new(secret, prepped.body, digestmod=hashlib.sha512)
# prepped.headers['Sign'] = signature.hexdigest()
#
# with requests.Session() as session:
#     response = session.send(prepped)