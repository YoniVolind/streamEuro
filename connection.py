import pathlib

import pathlib as pathlib
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from pathlib import Path
import time

def clear_my_cache():
    st.cache_data.clear()

st.title("יורו 2024 - פלוגה ב', 8132"+":punch:")
st.button('Refresh!', on_click=clear_my_cache,use_container_width=True)
col1,col2=st.columns(2)

css_file= "./styles/main.css"
with open(css_file,'r') as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)







# st.button('Refresh!', on_click=clear_my_cache,use_container_width=True)


conn = st.connection("gsheets", type=GSheetsConnection)
ttl_seconds = 10
# data = conn.read(worksheet='Games', ttl=ttl_seconds, usecols=list(range(6)))
# st.dataframe(data)

sql='''
select "Game Number","Side a","Side b", "Score a", "Score b"
from
Games
where
"Game Number" is not null
'''
df1=conn.query(sql=sql, ttl=ttl_seconds)
with col1:
    st.markdown("לוח המשחקים והתוצאות")
    st.dataframe(df1, height=700,width=500,hide_index=True)

sql1='''
select "rank","name","points"
from
Players
where
cast("rank" as integer) < 5
and cast("points" as integer) >0
order by "rank"

'''
df=conn.query(sql=sql1, ttl=ttl_seconds)
with col2:
    st.markdown("טבלת המובילים")
    st.dataframe(df,hide_index=True)




