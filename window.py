import tkinter as tk

import windowUtils
import const_enum as const

root = tk.Tk()  # メインウィンドウの作成
root.title(const.TITLE)
root.geometry(const.GEOMETRY)  # ウィンドウサイズ設定

option1 = tk.BooleanVar()
check = tk.Checkbutton(root, text="オプション", variable=option1)

options = [option1]
check.pack()


def on_click():
    windowUtils.on_click(options)


# スタートボタンの追加
start_button = tk.Button(root, text=const.START_BUTTON_TEXT, command=on_click)
start_button.pack()

root.mainloop()
