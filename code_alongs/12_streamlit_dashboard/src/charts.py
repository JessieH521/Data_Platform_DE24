from read_data import read_data
import duckdb
import streamlit as st

def approved_by_area_bar():

    df = read_data()

    # 想看不同领域学校的申请专业情况
    df = duckdb.query("""
                    select 
                        Utbildningsområde, count(*) as Beviljade
                    from df 
                    where 
                        Beslut == 'Beviljad'
                    group by 
                        Utbildningsområde
                    order by
                        Beviljade desc

                    """).df()

    # 建一个柱状图
    st.bar_chart(df, x= "", y= )
