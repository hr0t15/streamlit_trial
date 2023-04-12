# -*- coding: utf-8 -*-

import streamlit as st
from datetime import date


def main():
    markdown = """ 
    # input
    """
    st.markdown(markdown)
    markdown = """ 
    ## 1. Date インプット
    """
    st.markdown(markdown)

    birthday = st.date_input('When is your birthday?',
                             min_value=date(1900, 1, 1),
                             max_value=date.today(),
                             value=date(2000, 1, 1),
                             )
    st.write('Birthday: ', birthday)

    markdown = """ 
    ## 2. Time インプット
    """
    st.markdown(markdown)
    time = st.time_input(label='Your input:')
    st.write('input: ', time)

    markdown = """ 
    ## 3. 文字列入力

    一行の文字列の入力にはテキストインプットが使える。
    """
    st.markdown(markdown)
    text = st.text_input(label='Message', value='Hello, World!')
    st.write('input: ', text)

    markdown = """ 
    同様に、複数行に渡る文字列を入力するときはテキストエリアを用いる。
    """
    st.markdown(markdown)
    textarea = st.text_area(label='Multi-line message', value='Hello, World!')
    st.write('input: ', textarea)

    markdown = """ 
    ## 4. 数字入力
    """
    st.markdown(markdown)
    n = st.number_input(label='What is your favorite number?',
                        value=42,
                        )
    st.write('input: ', n)

    markdown = """ 
    デフォルト値を浮動小数点型にすれば、小数を入力できる。
    """
    st.markdown(markdown)
    num = st.number_input(label='What is your favorite number?',
                        value=3.14,
                        )
    st.write('input: ', num)


if __name__ == '__main__':
    main()