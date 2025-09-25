# --- 3. 辞書 (dictionary) ---
# キー(key)と値(value)をペアで保存するデータ型です。
# リストが番号（インデックス）で値を管理するのに対し、辞書は名前（キー）で値を管理します。
# 設定情報や、意味の明確なデータをまとめるのに便利です。

# --- 辞書の作成 ---
# {キー: 値, ...} のように作成します。キーは通常、文字列を使います。
camera_settings = {
    "name": "Webcam",
    "resolution_width": 1280,
    "resolution_height": 720,
    "fps": 30.0
}
print("カメラ設定:", camera_settings)

# --- 値へのアクセス ---
# キーを指定して値を取り出します。
camera_name = camera_settings["name"]
fps = camera_settings["fps"]
print("カメラ名:", camera_name)
print("FPS:", fps)

# --- 値の変更と追加 ---
camera_settings["fps"] = 60.0 # 既存のキーの値を更新
camera_settings["format"] = "MJPEG" # 新しいキーと値を追加
print("更新後のカメラ設定:", camera_settings)


# --- 練習問題 ---
# 1. ある画像ファイルに関する情報を保持する辞書 `image_info` を作成してください。
#    以下のキーと値を含めてください。
#    - "filename": "cat.jpg" (文字列)
#    - "width": 640 (整数)
#    - "height": 480 (整数)
#    - "has_alpha": False (真偽値)
#
# 2. `image_info` から、画像の幅 (width) を取り出して表示してください。
#
# 3. `image_info` に、新しいキー "author" と値 "Taro" を追加してください。
#
# 4. 追加後の `image_info` 辞書全体を表示してください。

# --- ここにコードを書いてください ---


# ------------------------------------
