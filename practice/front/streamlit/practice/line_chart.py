import streamlit as st
import numpy as np
import pandas as pd


# 데이터 생성
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randn(10)
})

# 그래프 그리기
st.line_chart(data['y'], use_container_width=True)

# 또는 아래와 같이 x, y를 따로 그래프로 그릴 수도 있습니다.
# st.line_chart(data[['x', 'y']], use_container_width=True)