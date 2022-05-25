import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "D:/System_File/Tesseract/tesseract.exe"


def findText(cvt_img):
    text = pytesseract.image_to_string(cvt_img)

    return text


def mark_letters(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

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


def detect_Word(img):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    words = []

    for idx, word in enumerate(boxes.splitlines()):
        if idx != 0:
            word = word.split()
            if len(word) == 12:
                words.append(word[11])
                x, y, w, h = int(word[6]), int(word[7]), int(word[8]), int(word[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 2)
                cv2.putText(img, word[11], (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


    return words


def detect_numbers(img):
    config = r'--oem 3 --psm 6 outputbase digits'

    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img,config=config)

    numbers = []

    for num in boxes.splitlines():
        num = num.split(' ')

        numbers.append(num[0])

        x, y, w, h = int(num[1]), int(num[2]), int(num[3]), int(num[4])
        cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (255, 0, 0), 2)
        cv2.putText(img, num[0], (x, hImg-y+25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

    return numbers