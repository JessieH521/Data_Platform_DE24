from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

# 将一个本地的 JSON 文件（jokes.json）中的数据发送到 Kafka 主题（jokes），代码使用了 quixstreams 库来简化 Kafka 的操作
# quixstreams.Application：这是 Quix Streams 提供的核心类，用于与 Kafka 集群交互，例如创建生产者、消费者或主题。

data_path = Path(__file__).parents[1] / "data"
# 索引 0 是当前路径的父目录，索引 1 是当前路径的上一级父目录，以此类推
# print(data_path)

# read from absolute path
with open(data_path / "jokes.json", "r", encoding="utf-8") as file:
    jokes = json.load(file)
    # 将 jokes.json 文件中的内容加载为 Python 字典或列表（取决于 JSON 的结构）
# pprint(jokes)

# create a Application instance and create a topic， 创建 Kafka Application 实例和主题
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")   
jokes_topic = app.topic(name="jokes", value_serializer="json")

# 指定 Kafka Broker 的地址（监听 9092 端口）, "text-splitter"：设置消费者组名称，用于标识客户端组。
# 指定 Kafka 的主题名称为 jokes, 设置主题的值序列化器为 JSON 格式。
# deserializer，不序列化，用于消费者（Consumer）。value_serializer，用于生产者（Producer）。

# print(jokes_topic)
      
# 发送消息到 Kafka
def main():
    with app.get_producer() as producer:    # 获取 Kafka 生产者对象，负责向 Kafka 主题发送消息。
        # print(producer)

        for joke in jokes:
            # (1) 序列化消息
            # serialize（序列化）一个过程，将复杂的数据结构（如对象、列表、字典等）转换成一种可以存储或传输的格式。消息数据转换为 Kafka 可识别和存储的格式。
            # deserialize（反序列化） 是将存储或传输的数据重新转换为原始的复杂数据结构。
            # value=joke 传递的是完整字典：{"joke_id": 1, "content": "Why did the chicken cross the road?"}，而不是某个值
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)
            print(f"Produced message: key={kafka_msg.key} value= {kafka_msg.value}")
            # (2) 发送消息到 Kafka
            producer.produce(topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value)
            # producer.produce() 是 Kafka Producer 的一个方法，用于生产消息（即将消息发布到 Kafka 的主题）
            # jokes 是 Kafka 中的一个逻辑消息队列，消息会被消费者从该主题读取。
            # key，键用于标识消息并帮助 Kafka 将消息分配到正确的分区
            # key 是序列化后的消息键，可能是字符串或数字。通过 str() 将其转换为字符串，确保键的格式符合 Kafka的要求
            # 是序列化后的消息内容，通常是 JSON 字符串或字节流，包含完整的笑话数据。

# run this code only when executing this script and not when importing this module
if __name__ == '__main__':
    
    # pprint(jokes)
    main()


# Terminal 里写：连接到本地的 Kafka 集群（localhost:9092），从 jokes 主题中消费消息，并从该主题的开始位置（包括历史消息）开始读取。
# kafka-console-consumer --bootstrap-server localhost:9092 --topic jokes --from-beginning
# 这个命令在运行时会不断地从 Kafka 主题 jokes 中消费消息，直到你手动停止它，Ctrl + C。或者像下面修改参数
# kafka-console-consumer --bootstrap-server localhost:9092 --topic jokes --from-beginning --timeout-ms 10000 ，只 消费 10 秒钟后停止； --max-messages 100，消费 100 条消息后停止。


# kafka_msg 是序列化后的 Kafka 消息，包含 key 和 value。
# 用途：
# 将 key 和 value 转换为 Kafka 能理解的格式（如 JSON）。
# 通过 Producer 发送到 Kafka 主题。
# 具体结构：
# kafka_msg.key：序列化后的消息键（通常是字符串）。
# kafka_msg.value：序列化后的消息值（通常是 JSON 字符串或字节流）。
# 在 Kafka 中，key 是可选的，但如果提供了 key：
# Kafka 会根据键的哈希值将消息分配到特定分区（Partition）。
# 使用相同 key 的消息会被分配到同一个分区，从而保证消息的顺序性。