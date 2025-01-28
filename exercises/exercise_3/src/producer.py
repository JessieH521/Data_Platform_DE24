from pathlib import Path
import json
import pandas as pd
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

with open(data_path / "orders.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

# # Iterate throuth each order
# for order in orders:
#     print(f"Order ID: {order['order_id']}")
#     print(f"Customer: {order['customer']}")
#     print(f"Order Date: {order['order_date']}")
#     print(f"Status: {order['status']}\n")

#     total_price = 0
#     data = []    # used for pandas

#     # Iterate through products in the order
#     for product in order["products"]:
#         name = product["name"]
#         price = product["price"]
#         quantity = product["quantity"]
#         total_item_price = price * quantity
#         total_price += total_item_price
#         data.append([name, quantity, price, total_item_price])
#         # 使用二维列表的结构很方便转换为 Pandas 的 DataFrame，方便后续分析和展示

#     #     # 用对齐规则 {:<25} 将产品名称等信息对齐到 25 个字符
#     #     print(f"Product: {name:<20}Quantity: {quantity:<5}Price: {price:<10.2f}Total Item Price: {total_item_price:.2f}")

#     # print(f"\nTotal Price: {total_price:.2f}")
#     # print("-" * 90)


#     # use Pandas
#     df = pd.DataFrame(data, columns=["Product", "Quantity", "Price", "Total Item Price"])
#     print(df.to_string(index=False, justify="left"))
#     # to_string() ，转换为一个格式化的字符串，方法会输出完整的数据表（没有省略。index=False ，索引会被隐藏
#     print(f"\nTotal Price: {total_price:.2f}")
#     print("-" * 80 + '\n')


# 1. 建 kafka 实例和主题
app = Application(broker_address="localhost:9092", consumer_group="order-splitter")
orders_topic = app.topic(name="orders", value_serializer="json")
# print(orders_topic)

# 2. 发送消息到 kafka
def main():
    with app.get_producer() as producer:
        for order in orders:
            # (1) 序列化消息
            kafka_msg = orders_topic.serialize(key=order["order_id"], value=order)
            print(f"Produced message: key={kafka_msg.key} value= {kafka_msg.value}")
            # (2) 发送消息到 Kafka
            producer.produce(topic="orders", key=str(kafka_msg.key),value=kafka_msg.value)


if __name__ == "__main__":
    main()




























