import streamlit as st
import random

# アプリのタイトル
st.title("帰国するか残るか？")

# ボタンを表示して、クリックされたら結果を表示
if st.button('結果を見る'):
    # 50%の確率で帰国するか残るかを決定
    result = random.choice(['帰国する', '残る'])
    st.write(f"結果: {result}")
