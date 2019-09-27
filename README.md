# Unofficial Binance Futures API w/ Sockets Support

**This is a work in progress. Use at your own risk**

This is an example of how to use binance futures API using websockets for streaming
data.

Make a pull request if you want to contribute.

# Quickstart
1. Create a `secret.py` file in your local repo with the API key and secret.
   Make sure you enable the future option

``` python
# secret.py

API_KEY="<BINANCE_API_KEY>"
API_SECRET="<BINANCE_API_SECRET>"
```

1. Install dependencies

``` shell
$ pip install -r requirements.txt
```

1. Run the `sockets.py`

``` shell
# list agents
$ python sockets.py
```

1. Use `rest.py` for misc rest endpoints

# TODO
1. Set up more streaming endpoints and parse the stream
1. Set up trading endpoints
1. Refactor shitty code into library eventually

# References
1. [Binance Futures API Reference](https://binance-docs.github.io/apidocs/futures/en/#change-log)
