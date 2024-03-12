"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2024-03-12
"""
from services.ocr.paddle_ocr import PADDLE

# TODO call paddleOCR service and show result
if __name__ == '__main__':
    image_path = ""
    paddle_ocr = PADDLE()
    paddle_ocr.detect_text(image=image_path)
