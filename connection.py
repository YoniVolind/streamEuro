import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time

st.title("יורו 2024")


conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(usecols=list(range(5)) ,worksheet='Games')
st.dataframe(data)



sql='''
select "id","rank","score"
from
Players
where
cast("rank" as integer) < 5

'''
df=conn.query(sql=sql)
st.dataframe(df)



