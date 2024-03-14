import sys
sys.path.append(r'D:\Python\visual-ocr-label\services\ocr')
import pytesseract_ocr

# TODO call pytesseract service and show result
if __name__ == '__main__':
    images_folder_path = "resources\image"
    pytesseract_ocr_obj = pytesseract_ocr.Tesseract()
    pytesseract_ocr_obj.extracted_tables_to_label_studio_json_file(images_folder_path)
