# Lecture 1 : 基本的な使い方

## Hello, Streamlit!

`st.write()` 関数は、任意のオブジェクトを WebUI に表示することができる。  
これを用いて、"Hello, Streamlit!"を表示させる。

このフォルダに`hello.py`というファイルを作成し、以下の通り記述する。

```python
import streamlit as st

st.write('Hello, Streamlit!')
```

`streamlit run` サブコマンドで指定して実行すると、
デフォルトでは 8501 ポートで Streamlit のアプリケーションサーバが起動する。

```
streamlit run hello.py
```

ブラウザより、出力結果を確認する。


## 基本的な書式

このフォルダに`basic.py`というファイルを作成し、以下の通り記述する。

Streamlit で表示可能な基本的な書式を以下の通り表示させる。

```python
import streamlit as st

# タイトル
st.title('タイトル')

# ヘッダ
st.header('ヘッダー')
# テキスト
st.text('単純なテキストの出力1')

# サブレベルヘッダ
st.subheader('サブヘッダー')
# テキスト
st.text('単純なテキストの出力2')
```

以下のコマンドで起動させる。

```
streamlit run basic.py
```
