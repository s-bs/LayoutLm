"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2024-03-12
"""
import sys
sys.path.append(r'D:\Python\visual-ocr-label\services\ocr')
import paddle_ocr


# TODO call paddleOCR service and show result
if __name__ == '__main__':
    images_folder_path = "resources\image"
    paddle_ocr_obj = paddle_ocr.Paddle()
    paddle_ocr_obj.extracted_tables_to_label_studio_json_file_with_paddleOCR(images_folder_path)
