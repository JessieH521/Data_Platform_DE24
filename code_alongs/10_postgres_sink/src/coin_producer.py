import time
from quixstreams import Application
from constants import COINMARKET_API
from requests import Session, Timeout, TooManyRedirects  
# requests 库 提供的一种 会话管理（Session） 方式，用于在多个 HTTP 请求之间保持连接。
import json
from pprint import pprint

app = Application(broker_address="localhost:9092", consumer_group="coin_group")

coins_topic = app.topic(name="coins", value_serializer="json")

# 从 CoinMarketCap API 获取指定加密货币（默认 BTC）的最新价格数据。
def get_latest_coin_data(symbol="BTC"):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        "symbol": symbol,     
        "convert": "USD",           
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,    
    }

    session = Session()         
    session.headers.update(headers)     

    try:
        response = session.get(url, params=parameters)    # 发送 HTTP GET 请求
        # return json.loads(response.text).get("data").get(symbol)     # 将返回的 JSON 转换为 Python 字典
        data = json.loads(response.text).get("data", {})
        return data.get(symbol, {})
    except (ConnectionError, Timeout, TooManyRedirects) as e:  # 网络连接问题，请求超时， 请求被重定向过多次
        print(e)


def main():

    with app.get_producer() as producer:
        while True:
            coin_latest = get_latest_coin_data("BTC")
            # pprint(latest_quotes)
            # coin_latest = latest_quotes["quote"]

            kafka_message = coins_topic.serialize(
                key=coin_latest["symbol"], value=coin_latest
            )
            print(
                f"produce event with key = {kafka_message.key}, price = {coin_latest['quote']['USD']['price']}"
            )
            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )


if __name__ == "__main__":
    # result = get_latest_coin_data("ETH")
    # pprint(result)
    main()















