import time

# from connect_crypto_api import Cryptocurrency
from quixstreams import Application
from constants import COINMARKET_API

from requests import Session
import json
from pprint import pprint

app = Application(
    broker_address="localhost:9092",
    consumer_group="coin_group",
)

coins_topic = app.topic(name="coins", value_serializer="json")


def get_latest_coin_data(symbol="BTC"):
    api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COINMARKET_API,
    }

    parameters = {
        "symbol": symbol,
        "convert": "USD",
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(api_url, params=parameters)
    return json.loads(response.text)["data"][symbol]


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
                f"produce event with key = {kafka_message.key}, value = {coin_latest['quote']['USD']['price']}"
            )
            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value
            )

            time.sleep(10)


if __name__ == "__main__":
    main()
    pprint(get_latest_coin_data("BTC")["quote"])
