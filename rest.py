#!/usr/bin/env python

import requests
import asyncio
import websockets
import ssl

import secret

API_KEY = secret.API_KEY
API_SECRET = secret.API_SECRET

BASE_URL = "https://fapi.binance.com/fapi/v1"

def get_orderbook(symbol="BTCUSDT", limit="100"):
    resp = requests.get(BASE_URL + "/depth",
                        params={
                            "symbol": symbol,
                            "limit": limit
                        })

    return resp.json()


if __name__ == '__main__':
    print(get_orderbook())
