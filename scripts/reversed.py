import streamlit as st


def reverse_text(text):
    """与えられたテキストを逆にする"""
    return text[::-1]


st.title("テキスト逆転アプリ")

user_input = st.text_input("テキストを入力してください:", "ここにテキストを入力")

if st.button("逆転!"):
    reversed_text = reverse_text(user_input)
    st.write("逆転したテキスト:", reversed_text)
