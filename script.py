

import ccxt


binancecoinm = ccxt.binancecoinm()
binance = ccxt.binance()
binanceusdm = ccxt.binanceusdm()
ftx = ccxt.ftx()
huobi = ccxt.huobi()
okex = ccxt.okex()
bitfinex = ccxt.bitfinex2()
bitmex = ccxt.bitmex()
bybit = ccxt.bybit()
coinbase = ccxt.coinbase()
coinbaseprime = ccxt.coinbaseprime()
coinbasepro = ccxt.coinbasepro()
deribit = ccxt.deribit()
hitbtc = ccxt.hitbtc()
kraken = ccxt.kraken()
kucoin = ccxt.kucoin()
kucoinfutures = ccxt.kucoinfutures()
okex = ccxt.okex()
phemex = ccxt.phemex()

dd = {
    "\33[33mbinance coin-m futs\033[0m": binancecoinm.fetch_ticker("BTC/USD")["last"],
    "\33[33mbinance usd futs\033[0m": binanceusdm.fetch_ticker("BTCUSDT")["last"],
    "\033[96mftx usd futs\033[0m\t": ftx.fetch_ticker("BTC-PERP")["last"],
    "phemex inverse futs": phemex.fetch_ticker("BTCUSD")["last"],
    "phemex linear futs": phemex.fetch_ticker("BTC/USDT")["last"],
    "okex linear futs":okex.fetch_ticker("BTC-USDT-SWAP")["last"],
    "okex inverse futs":okex.fetch_ticker("BTC-USD-SWAP")["last"],
    "kucoin usdt futs":kucoinfutures.fetch_ticker("XBTUSDTM")["last"],
    "kucoin usd futs":kucoinfutures.fetch_ticker("XBTUSDM")["last"],
    "\33[92mderibit usd futs\033[0m":deribit.fetch_ticker("BTC-PERPETUAL")["last"],
    "\033[1;31mbybit linear futs\033[0m":bybit.fetch_ticker("BTCUSDT")["last"],
    "\033[1;31mbybit inverse futs\033[0m":bybit.fetch_ticker("BTCUSD")["last"],
    "\033[94mbitmex us\033[0m\033[1;31md futs\033[0m":bitmex.fetch_ticker("BTC/USD")["last"],
    "\033[94mbitmex us\033[0m\033[1;31mdt futs\033[0m":bitmex.fetch_ticker("BTC/USDT")["last"],
    "\033[92mbitfinex usd futs\033[0m":bitfinex.fetch_ticker("tBTCF0:USTF0")["last"],


    # "\033[94mcoinbasepro usdt spot\033[0m":coinbasepro.fetch_ticker("BTC/USDT")["last"],
    # "\033[94mcoinbasepro usd spot\033[0m":coinbasepro.fetch_ticker("BTC/USD")["last"],
    # "\033[94mcoinbasepro usdc spot\033[0m":coinbasepro.fetch_ticker("BTC/USDC")["last"],
    # "coinbase usd spot":coinbase.fetch_ticker("BTC/USD")["last"],
    # "kucoin usdt spot":kucoin.fetch_ticker("BTC/USDT")["last"],
    # "kraken usd spot":kraken.fetch_ticker("BTC/USD")["last"],
    # "kraken usdt spot":kraken.fetch_ticker("BTC/USDT")["last"],    
    # "hitbtc usdt spot":hitbtc.fetch_ticker("BTC/USDT")["last"],
    # "okex usdt spot\t":okex.fetch_ticker("BTC/USDT")["last"],
    # "\033[96mftx USDT spot\033[0m\t": ftx.fetch_ticker("BTC/USDT")["last"],
    # "\033[96mftx USD spot\033[0m\t": ftx.fetch_ticker("BTC/USD")["last"],
    # "\33[33mbinance usdt spot\033[0m": binance.fetch_ticker("BTC/USDT")["last"],
    # "\033[92mbitfinex usd spot\033[0m":bitfinex.fetch_ticker("tBTCUSD")["last"],
    # "\033[92mbitfinex usdt spot\033[0m":bitfinex.fetch_ticker("BTC/USDT")["last"],
    # "huobi usdt spot":huobi.fetch_ticker("BTC/USDT")["last"],
    # "huobi usdd spot":huobi.fetch_ticker("BTC/USDC")["last"],

}

srt = {k: v for k, v in sorted(dd.items(), key=lambda item: item[1], reverse=True)}
print("exchange name\t\t\t", "price\t\t", "delta from highest")
for x in srt:
    color = ""
    delta = round(srt[x] - srt[list(srt.keys())[int(len(list(srt.keys()))/2)]], 1)
    if delta < 0:
        color = "\33[31m"
    elif delta > 0:
        color = "\33[32m"
    else:
        color = "\33[34m"
    print(x, "\t\t" ,srt[x], "\t", color+str(delta) + "\033[0m")
