import requests


def about_get():
    return requests.get("https://api.exchange.trade.io/api/v1/about")


def time_get():
    return requests.get("https://api.exchange.trade.io/api/v1/time")