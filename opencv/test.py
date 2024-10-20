import cv2
from pytesseract import pytesseract


class TextRecognition:

    @staticmethod
    def text_recognition():
        # 识别数字和英文
        image = cv2.imread('/Users/tongziyu/Desktop/25cf957fd093427ca6f790620dcea32b.png')
        text = pytesseract.image_to_string(image, lang='eng', config='--psm 7')
        print(text)

        # 识别中文
        image = cv2.imread('/Users/tongziyu/Desktop/25cf957fd093427ca6f790620dcea32b.png')
        text = pytesseract.image_to_string(image, lang='chi_sim', config='--psm 6')
        print(text)


textRecognition = TextRecognition()
