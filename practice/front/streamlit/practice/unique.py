import streamlit as st


def test():
    print('test')

st.button('test', key='test', on_click=test)