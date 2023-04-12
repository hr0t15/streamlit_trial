# -*- coding: utf-8 -*-

import time

import streamlit as st
import numpy as np


def main():
    # 折れ線グラフ (初期状態)
    x = np.random.random(size=(10, 2))
    line_chart = st.line_chart(x)

    for i in range(10):
        # 折れ線グラフに 0.5 秒間隔で 10 回データを追加する
        additional_data = np.random.random(size=(5, 2))
        line_chart.add_rows(additional_data)
        time.sleep(0.5)


if __name__ == '__main__':
    main()