from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"
# 索引 0 是当前路径的父目录，索引 1 是当前路径的上一级父目录，以此类推
# print(data_path)

with open(data_path / "jokes.json", "r", encoding="utf-8") as file:
    jokes = json.load(file)
# pprint(jokes)

# create a application instance and create a topic
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")    # 在taml文档中找找
jokes_topic = app.topic(name="jokes", value_serializer="json")

# print(jokes_topic)

def main():
    with app.get_producer() as producer:
        # print(producer)

        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            print(f"Produced message: key={kafka_msg.key} value= {kafka_msg.value}")

            producer.produce(topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value)

# run this code only when executing this script and not when importing this module
if __name__ == '__main__':
    # pprint(jokes)
    main()







