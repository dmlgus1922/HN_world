import streamlit as st


if 'button_name' not in st.session_state:
    st.session_state.button_name = '못 쓰는 버튼'

if 'button_attr' not in st.session_state:
    st.session_state.button_attr = True

if 'change_button' not in st.session_state:
    st.session_state.change_button = False


btn = st.container()

if st.button('바꾸기', key='test2'):
    if st.session_state.button_name == '못 쓰는 버튼':
        st.session_state.button_name = '사용 가능'
        st.session_state.button_attr = False
    else:
        st.session_state.button_name = '못 쓰는 버튼'
        st.session_state.button_attr = True

btn.button(st.session_state.button_name, 
            key='test',
            disabled=st.session_state.button_attr)


st.session_state