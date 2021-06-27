import cv2
import numpy as np
import pandas as pd
import PIL.ImageOps
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = np.load("image.npz")["arr_0"]

y_df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/datasets/master/C%20122-123/labels.csv")

y = y_df["labels"]


print(pd.Series(y).value_counts())

classes = ['A','B','C','D','E','F','G','H','I','J',"K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
len_Classes = len(classes)


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, test_size=0.25)

X_train_scaled = X_train/255.0
X_test_scaled = X_test/255.0


classifier = LogisticRegression(solver='saga', multi_class='multinomial')
classifier.fit(X_train_scaled, y_train)


y_prediction = classifier.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, y_prediction)
print(accuracy)


# opening the camera
capture = cv2.VideoCapture(0)

while True:

        ret, frm = capture.read()
        grey = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

        height, width = grey.shape

        upper_left = (int(width/2-56), int(height/2-56))
        bottom_right = (int(width/2+56), int(height/2+56))

        cv2.rectangle(grey, upper_left, bottom_right, (0,255,0), 2)

        roi = grey[upper_left[1]:bottom_right[1], upper_left[0]: bottom_right[0]]

        img_pil = Image.fromarray(roi)

        img_bw = img_pil.convert('L')

        img_resized = img_bw.resize((28, 28), Image.ANTIALIAS)

        # import the img
        img_inverted = PIL.ImageOps.invert(img_resized)

        pixel_filter = 20

        # converting to scaler quantity
        min_pixel = np.percentile(img_inverted, pixel_filter)
        img_scaled = np.clip(img_inverted - min_pixel, 0, 255)
        max_pixel = np.max(img_inverted)

        # converting into an array
        img_final = np.asarray(img_scaled)/max_pixel

        # create a test sample and make a prediction
        test_sample = np.array(img_scaled).reshape(1, 784)

        test_prediction = classifier.predict(test_sample)
        print('Prediction: ',test_prediction)

        grey = np.flip(grey, axis=1)

        cv2.imshow('Frame', grey)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        
        
capture.release()
cv2.destroyAllWindows()
