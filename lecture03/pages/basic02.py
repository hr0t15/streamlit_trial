# -*- coding: utf-8 -*-

import streamlit as st


def main():
    # プレースホルダーを用意する
    placeholder1 = st.empty()
    # プレースホルダーに文字列を書き込む
    placeholder1.write('Hello, World')

    placeholder2 = st.empty()
    # コンテキストマネージャとして使えば出力先をプレースホルダーにできる
    with placeholder2:
        # 複数回書き込むと上書きされる
        st.write(1)
        st.write(2)
        st.write(3)  # この場合は最後に書き込んだものだけ見える


if __name__ == '__main__':
    main()