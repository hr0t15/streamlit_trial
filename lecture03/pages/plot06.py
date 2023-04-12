# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np


def main():
    x = np.random.random(size=(400, 400, 3))
    # NumPy 配列をカラー画像として可視化する
    st.image(x)


if __name__ == '__main__':
    main()