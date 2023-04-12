# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


def main():
    # Pandas のデータフレームを可視化してみる
    data = {
        # ランダムな値で初期化する
        'x': np.random.random(20),
        'y': np.random.random(20),
    }
    df = pd.DataFrame(data)
    # データフレームを書き出す
    st.dataframe(df)
    # st.write(df)  でも良い
    # スクロールバーを使わず一度に表示したいとき
    st.table(df)


if __name__ == '__main__':
    main()