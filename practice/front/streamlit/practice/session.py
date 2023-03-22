import streamlit as st


keys = 'light aircon computer'.split()

# Initialization
for key in keys:
    if key not in st.session_state:
        st.session_state[key] = 'off'


# Session State also supports attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'


light = st.button('전등')
aircon = st.button('에어컨')
computer = st.button('컴퓨터')

if light:
    st.session_state.light = 'on' if st.session_state.light == 'off' else 'off'

for key in keys:
    st.write(st.session_state[key])
    
st.write(st.session_state)