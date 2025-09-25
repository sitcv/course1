# --- 練習問題の解答例 ---

# --- 01_variables_and_types.py ---
print("--- 解答: 01 ---")
favorite_food = "カレー"
price = 900
print("好きな食べ物:", favorite_food, ", 値段:", price, "円")
print("-" * 20)


# --- 02_lists.py ---
print("--- 解答: 02 ---")
# 1
points = [[50, 100], [120, 80], [200, 250]]
# 2
y2 = points[1][1]
print("2点目のY座標:", y2)
# 3
points.append([300, 150])
# 4
print("追加後のpointsリスト:", points)
print("-" * 20)


# --- 03_dicts.py ---
print("--- 解答: 03 ---")
# 1
image_info = {
    "filename": "cat.jpg",
    "width": 640,
    "height": 480,
    "has_alpha": False
}
# 2
width = image_info["width"]
print("画像の幅:", width)
# 3
image_info["author"] = "Taro"
# 4
print("追加後のimage_info辞書:", image_info)
print("-" * 20)


# --- 04_loops.py ---
print("--- 解答: 04 ---")
points = [[50, 100], [120, 80], [200, 250], [300, 150]]
# 1
print("--- 各座標 ---")
for point in points:
    print(point)
# 2
print("--- 各X座標 ---")
for point in points:
    print("X座標:", point[0])
print("-" * 20)


# --- 05_conditionals.py ---
print("--- 解答: 05 ---")
pixels = [120, 255, 80, 200, 30, 150]
for p in pixels:
    if p >= 128:
        print(f"明るいピクセルです: {p}")
    else:
        print(f"暗いピクセルです: {p}")
print("-" * 20)


# --- 06_functions.py ---
print("--- 解答: 06 ---")
# 1
def calculate_area(width, height):
    return width * height
# 2
area = calculate_area(320, 240)
print(f"幅320, 高さ240 の面積は {area} です。")
print("-" * 20)


# --- 07_numpy_intro.py ---
print("--- 解答: 07 ---")
# この解答を実行するにはnumpyが必要です
try:
    import numpy as np
    # 1
    data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    data_array = np.array(data_list)
    # 2
    result_array = data_array * 5
    print("5倍した結果の配列:", result_array)
except ImportError:
    print("NumPyがインストールされていません。")
    print("uv pip install numpy を実行してください。")
print("-" * 20)
