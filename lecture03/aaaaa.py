# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date


def main():
    markdown = """ 
    # input
    """
    st.markdown(markdown)

    markdown = """ 
    ## 1. ボタン

    ボタンは `streamlit.button()` 関数を使って配置できる。 
    以下のサンプルコードは、ボタンを押すことで表示される内容が変わるものとなっている。 
    興味深いのは、ボタンにイベントハンドラなどの類が一切設定されていないこと。
    """
    st.markdown(markdown)

    # データフレームを書き出す
    data = np.random.randn(20, 3)
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    st.dataframe(df)
    # リロードボタン
    st.button('Reload')

    markdown = """ 
    ポイントは、Streamlit は毎回スクリプトを評価し直すように動作するところ。 
    つまり、ウィジェットで何らかのイベントが起こったら、
    Streamlit はページの内容を丸ごと評価し直すと考えれば良い。 
    上記のサンプルコードは、ボタンが押されるイベントによって、表示が丸ごと変わったわけだ。

    ウィジェットは、一番最後の試行 (評価) のときに、ウィジェットがどのような状態になったかを返す場合がある。 ボタンも同様で、最後の試行でボタンが押されたか・押されていないかを真偽値 (bool) で返す。

    ウィジェットの特性を利用すると、ウィジェットを設置する関数から返ってくる値を使ってインタラクティブな画面が作れる。 以下のサンプルコードでは、2 つのボタンを設置して、押されたボタンに対応するメッセージを表示している。
    """
    st.markdown(markdown)

    if st.button('Top button'):
        # 最後の試行で上のボタンがクリックされた
        st.write('Clicked')
    else:
        # クリックされなかった
        st.write('Not clicked')

    if st.button('Bottom button'):
        # 最後の試行で下のボタンがクリックされた
        st.write('Clicked')
    else:
        # クリックされなかった
        st.write('Not clicked')


    markdown = """ 
    ## 2. チェックボックス

    チェックボックスは、最後の試行でチェックされたか・されなかったかを元に処理を分岐できる。  
    以下のサンプルコードでは、チェックされたときだけデータフレームを表示している。
    """
    st.markdown(markdown)

    # チェックボックスにチェックが入っているかで処理を分岐する
    if st.checkbox('Show'):
        # チェックが入っているときはデータフレームを書き出す
        data = np.random.randn(20, 3)
        df = pd.DataFrame(data, columns=['x', 'y', 'z'])
        st.dataframe(df)

    markdown = """ 
    ## 3. ラジオボタン

    同様に、最後の試行でチェックされたアイテムを元に処理をできるラジオボタン。
    """
    st.markdown(markdown)

    # チェックボックスにチェックが入っているかで処理を分岐する
    selected_item = st.radio('Which do you like?',
                             ['Dog', 'Cat'])
    if selected_item == 'Dog':
        st.write('Wan wan')
    else:
        st.write('Nya- nya-')

    markdown = """ 
    ## 4. セレクトボックス
    """
    st.markdown(markdown)
    selected_item = st.selectbox('Which do you like?',
                                 ['Dog', 'Cat'])
    st.write(f'Selected: {selected_item}')

    markdown = """ 
    ### マルチセレクト

    単一のアイテムを選択するセレクトボックスの他に、複数のアイテムを選択できるマルチセレクトもある。
    """
    st.markdown(markdown)
    selected_items = st.multiselect('What are your favorite characters?',
                                    ['Miho Nishizumi',
                                     'Saori Takebe',
                                     'Hana Isuzu',
                                     'Yukari Akiyama',
                                     'Mako Reizen',
                                     ])
    st.write(f'Selected: {selected_items}')

    markdown = """ 
    ## 5. スライダー

    ### ベーシックなもの
    """
    st.markdown(markdown)
    age = st.slider(label='Your age',
                    min_value=0,
                    max_value=130,
                    value=30,
                    )
    st.write(f'Selected: {age}')

    markdown = """ 
    ### レンジを指定する

    デフォルトの値にタプルなどで 2 つの要素を指定すると、レンジを入力できるようになる。
    """
    st.markdown(markdown)
    min_value, max_value = st.slider(label='Range selected',
                                     min_value=0,
                                     max_value=100,
                                     value=(40, 60),
                                     )
    st.write(f'Selected: {min_value} ~ {max_value}')

    markdown = """ 
    ちなみに整数以外にも日付とかを指定するのにも使える。  
    ただ、そんなに使いやすいとは思えない。  
    日付とか時間は後述する専用のウィジェットを使った方が良いと思う。
    """
    st.markdown(markdown)
    birthday = st.slider('When is your birthday?',
                         min_value=date(1900, 1, 1),
                         max_value=date.today(),
                         value=date(2000, 1, 1),
                         format='YYYY-MM-DD',
                         )
    st.write('Birthday: ', birthday)


if __name__ == '__main__':
    main()
