import datetime

#######################
#   ジョブの定数を定義   #      パス関連は外部テキストファイルを参照するように修正する予定
#######################
# TESSERACT_CMDの保存先
TESSERACT_CMD = r'E:/dev/Tesseract-OCR/tesseract.exe'

# クリップボードに保存された画像の保存先
SAVE_CLIPBOARD_PICTURE = f"E:/dev/OCR_test/OCR.tmp.png"

# ジョブに使用するフォルダ
SCREENSHOT_FOLDER = f"E:/dev/OCR_test/"

# OCR読み取り言語
OCR_LANG = "jpn"

# 文字コード：utf-8
ENCODING_UTF8 = "utf-8"

# 拡張子：.png
FILE_EXTENSION_PNG = ".png"

# 拡張子：.txt
FILE_EXTENSION_TXT = ".txt"

# tesseract_layout設定値
TESSERACT_LAYOUT = 6

# 異常終了
ABNORMAL_END = 2

###########################
#   関数のメッセージを定義    #
###########################
# 関数"save_clipboard_picture"クリップボードに保存された画像が存在しない
SAVE_CLIPBOARD_PICTURE_NOT_EXIST_MESSAGE = "クリップボードに画像がありません"

# 関数"get_ocr_message"終了メッセージ
GET_OCR_MESSAGE_END_MESSAGE = "クリップボードに読み取った文字列を保存しました:"

# 関数"opt_output_log"出力メッセージ
OPT_OUTPUT_LOG_MESSAGE = "読み取り結果↓"

#######################
# ウィンドウの定数を定義  #
#######################
# タイトル
TITLE = "文字取得"

# ウィンドウサイズ設定
GEOMETRY = "300x80"

# 実行ボタン表示文字
START_BUTTON_TEXT = "実行"

# チェックボックス：ログ出力
CHK_OUTPUT_LOG = "ログ出力"

# 実行時の日付(yyyyMMdd)
TODAY = format(datetime.date.today(), '%Y%m%d')

# 実行時の時間(yyyy年MM月dd日hh時mm分ss秒)
EXECUTION_TIME = format(datetime.datetime.now(), "%Y年%m月%d日 %H時%M分%S秒")
