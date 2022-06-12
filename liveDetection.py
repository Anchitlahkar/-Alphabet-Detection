import cv2
from recognition import *
print('Start')
print('loaded')

capture = cv2.VideoCapture(0)
print('capture')

# help()
while True:
	ret, frm = capture.read()

	img_converted = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
	
	# text = findText(img_converted)
	# print(text)
	boxes = mark_letters(img_converted)

	x = None
	y = None
	w = None
	h = None

	for b in boxes.splitlines():
		hImg, wImg, _ = img_converted.shape
		b = b.split(' ')
		x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

		cv2.rectangle(img_converted, (x, hImg-y), (w, hImg-h), (255, 0, 0), 2)
		cv2.putText(img_converted, b[0], (x, hImg-y+25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

	cv2.rectangle(img_converted, (x, hImg-y), (w, hImg-h), (255, 0, 0), 2)
	cv2.putText(img_converted, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


	cv2.imshow('Result', img_converted)

	if cv2.waitKey(1) & 0xFF == ord('q'):
            break

