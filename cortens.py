import time                                                     #import all needed packages

import tensorflow.keras
import numpy as np
import cv2

np.set_printoptions(suppress=True)

model = tensorflow.keras.models.load_model('cor_incor_model.h5')           #select the trained model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

imga = cv2.imread('validity_box_for_check.png')
imga = cv2.resize(imga, (224, 224))

image_array = np.asarray(imga)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

prediction = model.predict(data)

for a in prediction:  # write the result in the "result" list
    if a[0] > a[1]:
        print("1")
    if a[0] < a[1]:
        print("0")

with open('result.txt', 'w') as result_file:
    if a[0] > a[1]:
        result_file.writelines("1")
    if a[0] < a[1]:
        result_file.writelines("0")
