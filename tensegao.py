import time                                                     #import all needed packages

import tensorflow.keras
import numpy as np
import cv2

np.set_printoptions(suppress=False)

model = tensorflow.keras.models.load_model('mod.h5')           #select the trained model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

result = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]         #create a list where the results will be stored


#all from "def ahe(0)" is basically the same so i will only explain "def ahe0()"

def ahe0():                                                            #create a function for predicting the first face
    imga = cv2.imread('face_0.png')                                    #read the first face
    imga = cv2.resize(imga, (224, 224))                                #upscale the face to from 80x80 to 224x224

    image_array = np.asarray(imga)                                          #idk what this does but its somehow
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1   #converting the image into something
    data[0] = normalized_image_array                                        #tensorflow understands

    prediction = model.predict(data)                                        #predict if it's an ahegao or not

    for a in prediction:                                                    #write the result in the "result" list
        print(a)                                                            #at position 0
        if a[0] > a[1]:
            result[0] = 1
        if a[0] < a[1]:
            result[0] = 0


def ahe1():
    imgb = cv2.imread('face_1.png')
    imgb = cv2.resize(imgb, (224, 224))

    image_array = np.asarray(imgb)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for b in prediction:
        print(b)
        if b[0] > b[1]:
            result[1] = 1
        if b[0] < b[1]:
            result[1] = 0


def ahe2():
    imgc = cv2.imread('face_2.png')
    imgc = cv2.resize(imgc, (224, 224))

    image_array = np.asarray(imgc)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for c in prediction:
        print(c)
        if c[0] > c[1]:
            result[2] = 1
        if c[0] < c[1]:
            result[2] = 0


def ahe3():
    imgd = cv2.imread('face_3.png')
    imgd = cv2.resize(imgd, (224, 224))

    image_array = np.asarray(imgd)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for d in prediction:
        print(d)
        if d[0] > d[1]:
            result[3] = 1
        if d[0] < d[1]:
            result[3] = 0


def ahe4():
    imge = cv2.imread('face_4.png')
    imge = cv2.resize(imge, (224, 224))

    image_array = np.asarray(imge)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for e in prediction:
        print(e)
        if e[0] > e[1]:
            result[4] = 1
        if e[0] < e[1]:
            result[4] = 0


def ahe5():
    imgf = cv2.imread('face_5.png')
    imgf = cv2.resize(imgf, (224, 224))

    image_array = np.asarray(imgf)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for f in prediction:
        print(f)
        if f[0] > f[1]:
            result[5] = 1
        if f[0] < f[1]:
            result[5] = 0


def ahe6():
    imgg = cv2.imread('face_6.png')
    imgg = cv2.resize(imgg, (224, 224))

    image_array = np.asarray(imgg)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for g in prediction:
        print(g)
        if g[0] > g[1]:
            result[6] = 1
        if g[0] < g[1]:
            result[6] = 0


def ahe7():
    imgh = cv2.imread('face_7.png')
    imgh = cv2.resize(imgh, (224, 224))

    image_array = np.asarray(imgh)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for h in prediction:
        print(h)
        if h[0] > h[1]:
            result[7] = 1
        if h[0] < h[1]:
            result[7] = 0


def ahe8():
    imgi = cv2.imread('face_8.png')
    imgi = cv2.resize(imgi, (224, 224))

    image_array = np.asarray(imgi)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    for i in prediction:
        print(i)
        if i[0] > i[1]:
            result[8] = 1
        if i[0] < i[1]:
            result[8] = 0


ahe0()                                                  #execute all the functions to predict all faces
ahe1()
ahe2()
ahe3()
ahe4()
ahe5()
ahe6()
ahe7()
ahe8()


with open('result.txt', 'w') as result_file:            #create the file where the result will be saved in
    if result[0] == 0:                                  #write the first result in the file
        result_file.writelines("0,")                    #this repeats for all faces and then this code is done
    if result[0] == 1:                                  #and main.py continues
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[1] == 0:
        result_file.writelines("0,")
    if result[1] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[2] == 0:
        result_file.writelines("0,")
    if result[2] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[3] == 0:
        result_file.writelines("0,")
    if result[3] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[4] == 0:
        result_file.writelines("0,")
    if result[4] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[5] == 0:
        result_file.writelines("0,")
    if result[5] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[6] == 0:
        result_file.writelines("0,")
    if result[6] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[7] == 0:
        result_file.writelines("0,")
    if result[7] == 1:
        result_file.writelines("1,")

with open('result.txt', 'a') as result_file:
    if result[8] == 0:
        result_file.writelines("0")
    if result[8] == 1:
        result_file.writelines("1")
