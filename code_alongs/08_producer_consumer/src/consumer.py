from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)
# auto_offset_reset: 从一开始的时候读，不是从新加消息的开始读。
# deserializer，不序列化，用于消费者（Consumer）。value_serializer，用于生产者（Producer）。
jokes_topic = app.topic(name="jokes", value_deserializer="json")

# 创建 DataFrame 对象, streaming Dataframe
sdf = app.dataframe(topic=jokes_topic)

sdf = sdf.update(lambda message: print(f"Input: {message}"))

# def split_words(message):
#     return [{"word": word} for word in message["joke_text"].split()]
# sdf = sdf.apply(split_words, expand=True)

sdf = sdf.apply(lambda message: [{"word": word} for word in message ["joke_text"].split()], expand=True)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf = sdf.update(lambda row: print(f"Output: {row}"))

if __name__ == "__main__":
    app.run()




# 实时数据：每次运行都持续加载
# quixstreams 库（一个用于处理实时流数据的框架）
# app.dataframe()：将主题 jokes_topic 的流式数据包装成一个类似 Pandas DataFrame 的流处理对象（sdf）。用途：方便对流中的数据进行批量处理、更新或分析。
# .update()：用来定义如何处理每条流式数据。
# lambda message: print(f"Input: {message}")：对每条流式消息执行操作，这里是简单地打印消息内容，类似调试。

# apply(): 对流中的每个 message（假设它是一个 JSON 对象）操作：从 message["joke_text"] 中提取笑话文本。
# 使用 .split() 按空格拆分笑话文本，得到一个单词列表。将每个单词包装成字典格式 {"word": word}。
# 最终返回一个包含单词字典的列表。{"word": "Why"}, {"word": "don’t"},...

# sdf.update()：对数据帧中的每一行（row）进行处理，类似于 apply，但用于执行一些动作，而不是转换数据。
# lambda row: print(f"Output: {row}")：对流式数据帧中的每一行进行操作。
# 将当前的 row 数据打印到控制台，格式为：Output: {row}。
# expand=True 会将列表中的每个元素展开成独立的一行。

# sdf["length"]：在流式数据帧中创建一个新列，列名为 length，记录了每个单词的长度。

# app.dataframe：创建一个数据流的 DataFrame 对象，绑定到指定的 topic。从应用中获取与 Kafka 消息绑定的流式 DataFrame
# app.Dataframe() 是一个类构造器，用于创建一个新的、自定义的 DataFrame 实例

# 特性	      app.dataframe()	        app.Dataframe()
# 类型	        方法	              类或构造函数
# 用法	动态获取或创建 DataFrame，通常绑定到数据流	创建新的 DataFrame 实例，静态方法
# 上下文  用于绑定到运行时的外部系统，如 Kafka topic	用于手动或静态创建对象
# 命名约定	方法命名小写（符合 Python 方法规范）	类名首字母大写（符合 Python 类名规范）
# 是否需要参数	需要动态参数（如 topic 或 schema）	通常不需要参数，直接初始化



