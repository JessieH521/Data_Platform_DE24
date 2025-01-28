from quixstreams import Application
import json

app = Application(
    broker_address="localhost:9092",
    consumer_group="order-splitter",
    auto_offset_reset="earliest"
)

orders_topic = app.topic(name="orders", value_deserializer="json")

# 创建 DataFrame 对象
sdf = app.dataframe(topic=orders_topic)

# sdf = sdf.update(lambda message: print(f"Input: {message}"))
# 将 message 转换成 JSON 格式的字符串，并使用 indent=2 来格式化输出（每层缩进 2 个空格），方便阅读。
sdf = sdf.update(lambda message: print(f"Input: {json.dumps(message, indent=2)}"))

def products(message):
    return [
        {"name": product["name"], "price": product["price"], "quantity": product["quantity"]}
        for product in message["products"]]

sdf = sdf.apply(products, expand=True)      # 会将列表中的每个元素展开成独立的一行。

# sdf = sdf.update(lambda row: print(f"Output: {row}"))
sdf = sdf.update(lambda row: print(f"Output: {json.dumps(row, indent=2)}"))

if __name__ == "__main__":
    app.run()

















