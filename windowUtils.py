import execution


# 実行するオプションを起動
def on_click(options):
    # オプション選択内容を取得
    for i, option in enumerate(options):
        print(f"オプション{i + 1}の状態: {option.get()}")  # TODO オプションを変数に分けて分岐する
    execution.execution()
