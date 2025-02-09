import streamlit as st
from kpis import approved_percentage, number_approved, total_applications, provider_kpis
from read_data import read_data

df = read_data()


# 在浏览器里显示标题 YH dashboard 2024 applications. st.markdown() 显示 Markdown 格式的文本，# 表示一级标题（H1）
def layout():
    st.markdown("# YH dashboard 2024 applications")
    st.markdown(
        "This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard."
    )
    st.markdown("## KPIs in Sweden")

    # 一个 metric, have a label and a value
    labels = ("total applications", "number approved", "approved percentage")
    # 创建一个包含 3 列的布局，并且返回一个包含这些列的列表
    cols = st.columns(3)
    kpis = (total_applications, number_approved, approved_percentage)  # values

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)

    st.markdown("## Simple statistics on a given provider")
    st.markdown("Search for an educational provider")

    # 创建一个下拉选择框（selectbox）, 第一个参数是标签, 第二个参数是一个列表或数组，表示下拉框中的选项,某一列并去重
    provider = st.selectbox(
        "Choose educational provider",
        df["Utbildningsanordnare administrativ enhet"].unique())  
    
    provider_applications, provider_approved = provider_kpis(provider)

    st.markdown(f"This education provider {provider} has applied for {provider_applications} educations and gotten {provider_approved} educations approved.")

    st.markdown("## Raw data")

    # 读取 pandas 数据
    st.dataframe(df)


if __name__ == "__main__":
    layout()
