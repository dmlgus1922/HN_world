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


# session_state가 없다면
st.title('Counter Example without session state')

count_value = 0
increment = st.button('Increment')
if increment:
    count_value += 1

decrement = st.button('Decrement')
if decrement:
    count_value -= 1
st.write('Count = ', count_value)


# session_state가 있다면
st.title('Counter Example with session state')

# count session_state에 init
if 'count' not in st.session_state:
    st.session_state.count = 0
    
# increment 버튼이 클릭되면 session_state의 count에 1을 더함
increment = st.button('Increment1')
st.write(increment)
if increment:
    st.session_state.count += 1
# decrement 버튼이 클릭되면 session_state의 count에 1을 더함
decrement = st.button('Decrement2')
if decrement:
    st.session_state.count -= 1
st.write('Count = ', st.session_state.count)