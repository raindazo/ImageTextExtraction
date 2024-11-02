import execution


# 実行するオプションを起動
def on_click(chk_options):
    # オプション選択内容を取得
    is_output_log = chk_options[0].get()
    execution.execution(is_output_log)
