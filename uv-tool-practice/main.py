import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # --- 1. numpyとopencvを使った画像処理 ---
    # 300x500の黒い画像を生成
    width, height = 500, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # 画像にテキストを描画
    text = "Hello, Computer Vision!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255) # 白色
    thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

    # --- 2. pandasを使ったデータ操作 ---
    # 簡単なデータフレームを作成
    data = {'名前': ['田中', '鈴木', '佐藤'],
            '年齢': [28, 34, 45]}
    df = pd.DataFrame(data)
    print("--- pandas DataFrame ---")
    print(df)
    print("-" * 25)


    # --- 3. matplotlibを使ったグラフ描画 ---
    # 簡単なプロットを作成
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)

    # --- ファイルへの出力 ---
    # outputフォルダがなければ作成
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 画像を保存
    image_path = os.path.join(output_dir, 'sample_image_with_text.png')
    cv2.imwrite(image_path, image)
    print(f"'{image_path}' に画像を保存しました。")

    # グラフを保存
    plot_path = os.path.join(output_dir, 'my_plot.png')
    plt.savefig(plot_path)
    print(f"'{plot_path}' にグラフを保存しました。")
    # plt.show() # GUI環境がある場合は表示

if __name__ == "__main__":
    main()
