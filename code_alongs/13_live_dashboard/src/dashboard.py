import streamlit as st          # 用于创建 Web 应用程序
from streamlit_autorefresh import st_autorefresh          # 可以自动刷新页面
from sqlalchemy import create_engine       # 用于创建数据库连接 postgres
import pandas as pd
from constants import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER)
from charts import line_chart

# a connection to postgres， 连接 PostgreSQL 数据库
connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"

# 创建 SQLAlchemy 数据库引擎，用于执行 SQL 查询
engine = create_engine(connection_string)

# 定义数据加载函数，用于执行 SQL 查询
def load_data(query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)   # 运行 SQL 语句，将查询结果存入 DataFrame
        df = df.set_index("timestamp")   # 将 timestamp 列设置为索引
        return df

# ciunt 自定刷新网页
# st_autorefresh() 是自动刷新页面 的方法，每 10 秒（10,000 毫秒）刷新一次页面，最多刷新 100 次，超出后就不再自动刷新。 
# key 是 Streamlit 组件的唯一标识符，防止页面刷新时组件重新初始化。如不加 key，可能会误认是不同的组件，导致重复创建组件  
count = st_autorefresh(interval=10 * 1000, limit=100, key="data_refresh")

# Step 1.在浏览器里显示标题 YH dashboard 2024 applications. live数据，如果没有count 这个要手动刷新网页，不是自动更新。
def layout():
    df = load_data("select * from bitcoin;")

    st.markdown("# Coin data")
    st.markdown("This will display live data from coin market API")
    st.markdown("Latest data")
    st.dataframe(df.tail())   # 展示df 数据后5行

    st.markdown("## Last price in USD for bitcoin")
    # df.index 必须是 时间序列数据（timestamp），否则可能导致 x 轴不正确
    price_chart = line_chart(x=df.index, y=df["price_usd"], title="price USD")

    # 在 Streamlit 页面上渲染 Matplotlib 图像
    st.pyplot(price_chart)

if __name__ == "__main__":
    layout()





















