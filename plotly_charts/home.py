import streamlit as st

st.markdown("""
# Streamlit theme for Plotly charts!

[https://plotly.streamlit.app/](https://plotly.streamlit.app/)の転記が基本  
ただし、一部情報を以下の通りに表示させる。
""")

'''
0201_Bar_Charts.py
0202_Bubble_Charts.py
0301_Candlestick_Charts.py
0302_Contour_Plots.py
0303_Customization.py
0401_Distplot.py
0402_Dot_Plots.py
0602_Figure_Factory Subplots.py
0603_Filled_Area_Plots.py
0604_Funnel_Charts.py
0701_Gantt.py
0801_Heatmaps.py
0802_Histograms.py
0803_Horizontal_Bar_Charts.py
0901_Icicle_Charts.py
1201_Line_And_Scatter.py
1202_Line_Charts.py
1601_Pie_Charts.py
1901_Sankey_Diagram.py
1902_Sunburst_Charts.py
2001_Table.py
2002_Ternary_Plots.py
2003_Time_Series.py
2004_Treemaps.py
2301_Waterfall_Charts.py
'''


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

