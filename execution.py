import utils

import const_enum as const


def execution(is_output_log):
    # クリップボードに保存された画像を保存
    screenshot_path = utils.save_clipboard_picture()

    if screenshot_path == const.ABNORMAL_END:
        return

    # ocr実行
    ocr_text = utils.execution_ocr(screenshot_path)

    # 文字列をクリップボードに保存
    utils.get_ocr_message(ocr_text)

    # ファイル内の.pngファイルを削除する
    utils.delete_png_files()

    if is_output_log:
        utils.opt_output_log(ocr_text)
