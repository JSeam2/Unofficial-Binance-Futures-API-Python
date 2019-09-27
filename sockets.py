#!/usr/bin/env python

# TODO: This is totally incomplete

import requests
import asyncio
import websockets
import ssl

import secret

API_KEY = secret.API_KEY
API_SECRET = secret.API_SECRET

BASE_URL = "https://fapi.binance.com/fapi/v1"
TICKER_URI = "wss://fstream.binance.com/ws/BTCUSDT@ticker"
# SOCKET_URI = ("wss://fstream.binance.com/stream?="
#               # "BTCUSDT@aggTrade/"
#               # "BTCUSDT@markPrice/"
#               # "BTCUSDT@depth/"
#               "BTCUSDT@ticker")

"""
SOCKETS
"""

async def ticker():
    async with websockets.connect(TICKER_URI) as websocket:
        data = await websocket.recv()
        print(data)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(ticker())
