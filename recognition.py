import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "D:/System_File/Tesseract/tesseract.exe"

commands = {

    'findText': [
        'args: image (in the form of RBG)',
        'returns every text and numbers present in a img'
    ],

    'mark_letters': [
        'args: image (in the form of RBG)',
        'display the given img with added boxes around letters'
    ],

    'detect_Word': [
        'args: image (in the form of RBG)',
        'retuens words present in a img'
    ],

    'detect_numbers': [
        'args: image (in the form of RBG)',
        'returns numbers present in a img'
    ]
}


def help():
    for i in commands:
        print(f'{i}: \n\t {commands[i][0]} \n\t {commands[i][1]}\n')


def findText(cvt_img):
    text = pytesseract.image_to_string(cvt_img)

    return text


def mark_letters(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    return boxes

"""
    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (255, 0, 0), 2)
        cv2.putText(img, b[0], (x, hImg-y+25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)
"""

def detect_Word(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    words = []

    for idx, word in enumerate(boxes.splitlines()):
        if idx != 0:
            word = word.split()
            if len(word) == 12:
                words.append(word[11])
                x, y, w, h = int(word[6]), int(
                    word[7]), int(word[8]), int(word[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 2)
                cv2.putText(img, word[11], (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    return words


def detect_numbers(img):
    config = r'--oem 3 --psm 6 outputbase digits'

    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img, config=config)

    numbers = []

    for num in boxes.splitlines():
        num = num.split(' ')

        numbers.append(num[0])

        x, y, w, h = int(num[1]), int(num[2]), int(num[3]), int(num[4])
        cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (255, 0, 0), 2)
        cv2.putText(img, num[0], (x, hImg-y+25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    return numbers
