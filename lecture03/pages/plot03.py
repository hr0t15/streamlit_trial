# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
from matplotlib import pyplot as plt


def main():
    # 描画領域を用意する
    fig = plt.figure()
    ax = fig.add_subplot()
    # ランダムな値をヒストグラムとしてプロットする
    x = np.random.normal(loc=.0, scale=1., size=(100,))
    ax.hist(x, bins=20)
    # Matplotlib の Figure を指定して可視化する
    st.pyplot(fig)


if __name__ == '__main__':
    main()