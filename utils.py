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
        print(f"{const.SAVE_CLIPBOARD_PICTURE_EXIST_MESSAGE}{save_folder}")
        return save_folder
    else:
        print(const.SAVE_CLIPBOARD_PICTURE_NOT_EXIST_MESSAGE)
        return const.ABNORMAL_END


# ocr実行
def execution_ocr(screenshot):
    pyocr.tesseract.TESSERACT_CMD = const.TESSERACT_CMD

    # ツール取得
    tools = pyocr.get_available_tools()[0]

    img = Image.open(screenshot)
    builder = pyocr.builders.TextBuilder(tesseract_layout=const.TESSERACT_LAYOUT)
    return tools.image_to_string(img, lang=const.OCR_LANG, builder=builder)


# 文字列をクリップボードに保存
def get_ocr_message(text):
    pyperclip.copy(text)
    print(f"{const.GET_OCR_MESSAGE_END_MESSAGE}{text}")


# ファイル内の.pngファイルを削除する
def delete_png_files():
    for tidying in os.listdir(const.SCREENSHOT_FOLDER):
        if tidying.endswith(const.FILE_EXTENSION_PNG):
            file_path = os.path.join(const.SCREENSHOT_FOLDER, tidying)
            os.remove(file_path)
    print(const.DELETE_PNG_FILES_END_MESSAGE)


# ログ出力
def opt_output_log():
    file_path = os.path.join(const.SCREENSHOT_FOLDER, f"{const.TODAY}{const.FILE_EXTENSION_TXT}")
    # TODO 出力する内容を考える
    # TODO エラー時、通常終了時でエラー内容を変更する
