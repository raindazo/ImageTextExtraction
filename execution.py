import utils

import const_enum as const


def execution():
    # クリップボードに保存された画像を保存
    screenshot_path = utils.save_clipboard_picture()

    if screenshot_path != const.ABNORMAL_END:
        # ocr実行
        ocr_text = utils.execution_ocr(screenshot_path)

        # 文字列をクリップボードに保存
        utils.get_ocr_message(ocr_text)

        # ファイル内の.pngファイルを削除する
        utils.delete_png_files()
