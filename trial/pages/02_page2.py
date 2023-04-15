import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


# sidemenu
st.sidebar.markdown(
    "# Qiita sample"
)
template = st.sidebar.selectbox(
    "Template", list(pio.templates.keys())
)


st.markdown("""
これはStreamlitのアプリのサンプルです。
""")

@st.cache_data
def get_chart_49243206():
    import plotly.express as px
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

mpl = '''
@st.cache_data
def get_chart_49243206():
    import plotly.express as px
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
'''

st.code(mpl, 'python')
st.write(mpl)

get_chart_49243206()

# data
data = px.data.iris()


# body
st.write(
    px.scatter(data, x="sepal_width", y="sepal_length", template=template)
)