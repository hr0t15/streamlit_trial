# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


# 関数の出力をキャッシュする
@st.cache_data
def cached_data():
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20),
    }
    df = pd.DataFrame(data)
    return df


def main():
    # リロードしても同じ結果が得られる
    df = cached_data()
    st.dataframe(df)


if __name__ == '__main__':
    main()