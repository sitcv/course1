# --- 7. NumPy入門 ---
# NumPy(ナンパイ)は、Pythonで数値計算、特に多次元配列を効率的に扱うためのライブラリです。
# 画像はピクセルの多次元配列として扱われるため、コンピュータビジョンでは必須のツールです。

# !!! 注意 !!!
# このスクリプトを実行する前に、NumPyをインストールする必要があります。
# ターミナルで以下のコマンドを実行してください (`uv-tool-practice`での練習を思い出しましょう)。
# uv pip install numpy

import numpy as np

# --- NumPy配列 (ndarray) の作成 ---
# PythonのリストからNumPy配列を作成できます。
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Pythonリスト:", my_list)
print("NumPy配列:", my_array)

# --- NumPy配列の利点: 要素ごとの計算 ---
# NumPy配列を使うと、ループを使わずに全ての要素に対して一度に計算ができます。
# これを「ブロードキャスティング」と呼び、非常に高速です。
added_array = my_array + 10
multiplied_array = my_array * 2
print("全要素に10を足す:", added_array)
print("全要素を2倍する:", multiplied_array)

# --- 2次元配列 (行列) ---
# 画像データのように、縦横にデータが並ぶ場合は2次元配列を使います。
image_mock = np.array([
    [0, 128, 255],
    [50, 150, 200],
    [100, 180, 250]
])
print("--- 2次元配列 (画像の模倣) ---")
print(image_mock)
print("配列の形状 (shape):", image_mock.shape) # (行数, 列数)


# --- 練習問題 ---
# 1. 0から9までの数値を含む `data_list` というPythonリストがあります。
data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#    このリストを元に、`data_array` というNumPy配列を作成してください。
#
# 2. `data_array` の全ての要素を5倍した新しい配列 `result_array` を作成し、
#    `result_array` を表示してください。

# --- ここにコードを書いてください ---


# ------------------------------------
