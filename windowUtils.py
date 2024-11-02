import tkinter as tk
import execution


# 実行するオプションを起動
def on_click(options):
    for i, option in enumerate(options):
        print(f"オプション{i + 1}の状態: {option.get()}")
    execution.execution()
