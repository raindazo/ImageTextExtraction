import os

import pyperclip
import pyocr
from PIL import ImageGrab
from PIL import Image

import const_enum as const


# クリップボードに保存された画像を保存
def save_clipboard_picture():
    save_folder = os.path.expanduser(const.SAVE_CLIPBOARD_PICTURE)

    image = ImageGrab.grabclipboard()

    if isinstance(image, Image.Image):
        image.save(save_folder)
        print(f"クリップボードの画像を保存しました：{save_folder}")
        return save_folder
    else:
        print("クリップボードに画像がありません")
        return const.ABNORMAL_END


# ocr実行
def execution_ocr(screenshot):
    pyocr.tesseract.TESSERACT_CMD = const.TESSERACT_CMD

    # ツール取得
    tools = pyocr.get_available_tools()[0]

    img = Image.open(screenshot)
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    return tools.image_to_string(img, lang='jpn', builder=builder)


# 文字列をクリップボードに保存
def get_ocr_message(text):
    pyperclip.copy(text)
    print(f"クリップボードに保存読み取った文字列を保存しました:{text}")


# ファイル内の.pngファイルを削除する
def delete_png_files():
    for tidying in os.listdir(const.SCREENSHOT_FOLDER):
        if tidying.endswith('.png'):
            file_path = os.path.join(const.SCREENSHOT_FOLDER, tidying)
            os.remove(file_path)
    print("お片付け完了！")
