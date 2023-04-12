# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


def main():
    # ランダムな値でデータフレームを初期化する
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20) - 0.5,
        'z': np.random.random(20) - 1.0,
    }
    df = pd.DataFrame(data)
    # 折れ線グラフ
    st.subheader('Line Chart')
    st.line_chart(df)
    # エリアチャート
    st.subheader('Area Chart')
    st.area_chart(df)
    # バーチャート
    st.subheader('Bar Chart')
    st.bar_chart(df)


if __name__ == '__main__':
    main()