import tkinter as tk

import windowUtils
import const_enum as const


# ボタン押下時に引数を渡す
def on_click():
    windowUtils.on_click(options)


#######################
#    メインウィンドウ    #
#######################
root = tk.Tk()
root.title(const.TITLE)
root.geometry(const.GEOMETRY)

#######################
#    ウィンドウ設置物    #
#######################
# ログを保存する
var_output_log = tk.BooleanVar()
chk_output_log = tk.Checkbutton(root, text=const.CHK_OUTPUT_LOG, variable=var_output_log)

options = [var_output_log]
chk_output_log.pack()

# 実行ボタン設置
start_button = tk.Button(root, text=const.START_BUTTON_TEXT, command=on_click)
start_button.pack()

root.mainloop()
