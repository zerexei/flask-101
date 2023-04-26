from PIL import Image

import pytesseract
import re


class Tesseract:
    def parse(self, image_file):
        image = Image.open(image_file)
        ocr = pytesseract.image_to_string(image).rstrip()
        return (ref := re.search('Reference No. ([\w\d]+)', ocr)) and ref.group(1)