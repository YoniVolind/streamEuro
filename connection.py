import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time

st.title("יורו 2024")


conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(worksheet='Games',usecols=list(range(6)))
st.dataframe(data)

sql='''
select "Game Number","Side a","Side b", "Score a", "Score b"
from
Games
where
"Game Number" is not null
'''
df1=conn.query(sql=sql)
st.dataframe(df1, height=700,width=500)

sql1='''
select "rank","name","points"
from
Players
where
cast("rank" as integer) < 5
and cast("points" as integer) >0
order by "rank"

'''
df=conn.query(sql=sql1)
st.dataframe(df)


