import streamlit as st
import numpy as np

st.title('可視化図の表示の仕方')

# ランダムな値をヒストグラムとしてプロットする
data = np.random.normal(loc=.0, scale=1., size=(100,))

# --------------------------------
st.subheader('matplotlib')

st.code('''
from matplotlib import pyplot as plt

# 描画領域を用意する
fig = plt.figure()
ax = fig.add_subplot()
ax.hist(data, bins=30)
# Matplotlib の Figure を指定して可視化する
st.pyplot(fig)
''', "python")

from matplotlib import pyplot as plt

# 描画領域を用意する
fig = plt.figure()
ax = fig.add_subplot()
ax.hist(data, bins=30)
# Matplotlib の Figure を指定して可視化する
st.pyplot(fig)

# --------------------------------
st.subheader('plotly')

st.code("""
import plotly.express as px

fig = px.histogram(data, nbins=30)
st.plotly_chart(fig)
""", "python")

import plotly.express as px

fig = px.histogram(data, nbins=30)
st.plotly_chart(fig)
