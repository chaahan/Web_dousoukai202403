# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:15:29 2023

@author: 81801
"""

import streamlit as st
import pandas as pd



st.write("<h1>水戸桜ノ牧高等学校の<br>プチ同窓会案内</h1>", unsafe_allow_html=True)
st.caption('本同窓会は個人的に主催する者でオフィシャルなものではありません。')

st.write("現在、参加予定の方は以下です。")

df = pd.read_csv('meibo.csv',index_col='No.')
st.dataframe(df)


st.write("参加をする場合は以下二つの方法で")
st.write("　　１．幹事の飯田、もしくは安達に何でもいいので連絡をする")
st.write("　　   LINE,instgram何でもいいです")
st.write("　　　（代表して一人の人が、「〇〇と××と△△が参加します」みたいなのでもOK）")
st.write("　 ２．以下入力フォームより入力")


name = st.text_input("氏名")
plan = st.selectbox("参加可否",["参加","シフト次第で参加","参加したけど未定"])

clicked = st.button("登録")

