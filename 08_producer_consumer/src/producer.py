from quixstreams import Application
from pathlib import Path
import json

# consumer group allows parallel processing
app = Application(broker_address="localhost:9092", consumer_group="text-splitter-v1")

# topic with chat messages in json format
jokes_topic = app.topic(name="jokes", value_serializer="json")

jokes_path = Path(__file__).parent / "jokes.json"

with open(jokes_path, "r", encoding="utf-8") as file:
    jokes = json.load(file)


def main():
    print(app)
    with app.get_producer() as producer:
        for joke in jokes:
            joke["joke_id"] = str(joke["joke_id"])
            # serialize joke to send to Kafka topic called jokes
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            # print(jokes_topic.name)

            print(
                f"produce event with key = {kafka_msg.key}, value = {kafka_msg.value}"
            )

            producer.produce(
                topic=jokes_topic.name, key=kafka_msg.key, value=kafka_msg.value
            )


if __name__ == "__main__":
    main()
