from unittest.mock import MagicMock
from tradeioapi.api.about import about_get, time_get
from tradeioapi.api.trading import account_get
import requests


def setup_module():
    pass
    # with open('./tradeiobot/test/data_cmcexchanges.html') as f:
    #     mock = MagicMock(return_value=dotdict(dict(content=f.read())))
    #     requests.get = mock

def test_about_get():
    requests.get = MagicMock()
    r = about_get()
    requests.get.assert_called_once_with('https://api.exchange.trade.io/api/v1/about')

def test_time_get():
    requests.get = MagicMock()
    r = time_get()
    requests.get.assert_called_once_with('https://api.exchange.trade.io/api/v1/time')

def test_account_get():
    pass
    # a = account_get("mykey", "mysecret")
    # assert a == 1