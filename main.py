#first of all: huge thanks to Chill from the discord server "Hello World!"
#he helped me a lot with programming this

#selenium imports (for browser interaction)
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#PIL Import (for croping the entire iframe to the single faces)
from PIL import Image

#time import (just for delays)
import time

captchaURL = "https://captcha.ahegao.li"    #URL for the captcha (this Code only works for the Ahegao Captcha)
waitTime = 2                                #general purpose delay time
eaTime = 0.2                                #error avoiding time
loadTime = 2                                #how long the site has to load fully
                                            # (you might have to change this if you have slow internet)
driver = webdriver.Firefox()                #selection of the browser for the geckodriver (geckodriver.exe)

action_chains = ActionChains(driver)        #I actually don't know what these two do, but they're needed for clicking
action = webdriver.common.action_chains.ActionChains(driver)

driver.get(captchaURL)                                          #open the Website of the captcha

time.sleep(loadTime)                                            # delay to avoid "element not found" error
box_iframe = driver.find_element(By.ID, value="captcha-wrapper")#get the iframe where the box is positioned

action.move_to_element_with_offset(box_iframe, 20, 38)          #move the "cursor" above the box...
action.click()                                                  #and click it
action.perform()                                                #this is needed for the click to work

time.sleep(waitTime)                                            #wait for the faces to fully show

element = driver.find_elements(By.TAG_NAME, value="iframe")     #select the iframe containing the faces
element[0].screenshot('ahegao_uncroped.png')

all_faces = Image.open('./ahegao_uncroped.png')                 #select the screenshot to be croped
xy_crop_values_0 = (1, 80, 80, 160)                             #x/y values for croping face 0
face_0 = all_faces.crop(xy_crop_values_0)                       #crop face 0
face_0.save('face_0.png')                                       #save the image for tensorflow
                                                                #everything until time.sleep(60) is just croping
all_faces = Image.open('./ahegao_uncroped.png')                 #all remaining faces, so I will not comment it
xy_crop_values_1 = (81, 81, 160, 160)
face_1 = all_faces.crop(xy_crop_values_1)
face_1.save('face_1.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_2 = (161, 81, 240, 160)
face_2 = all_faces.crop(xy_crop_values_2)
face_2.save('face_2.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_3 = (1, 161, 80, 240)
face_3 = all_faces.crop(xy_crop_values_3)
face_3.save('face_3.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_4 = (81, 161, 160, 240)
face_4 = all_faces.crop(xy_crop_values_4)
face_4.save('face_4.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_5 = (161, 161, 240, 240)
face_5 = all_faces.crop(xy_crop_values_5)
face_5.save('face_5.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_6 = (1, 241, 80, 320)
face_6 = all_faces.crop(xy_crop_values_6)
face_6.save('face_6.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_7 = (81, 241, 160, 320)
face_7 = all_faces.crop(xy_crop_values_7)
face_7.save('face_7.png')

all_faces = Image.open('./ahegao_uncroped.png')
xy_crop_values_8 = (161, 241, 241, 320)
face_8 = all_faces.crop(xy_crop_values_8)
face_8.save('face_8.png')

os.system("del ahegao_uncroped.png")                         #remove the uncroped image because it's not needed anymore
os.system("python tensegao.py")                              #start tensorflow(tensegao.py)

time.sleep(1)                                                #wait for tensorflow(tensegao.py) to completly end

element = driver.find_elements(By.TAG_NAME, value="iframe")

txt_file = open("result.txt", "r")                            #open the file which tensorflow saved the results in
file_content = txt_file.read()                                #read the results
result_list = file_content.split(",")                         #put the results into a python list
txt_file.close()                                              #close the file

box_iframe = driver.find_element(By.ID, value="captcha-wrapper")#select the iframe where the box is positioned

action.move_to_element_with_offset(box_iframe, 20, 38)          #move the "cursor" above the box...
action.click()                                                  #and click it
action.perform()                                                #this is needed for the click to work

if result_list[0] == "1":                                       #check if the face came back as ahegao-positive if yes:
    action.move_to_element_with_offset(element[0], 44, 120)     #move the "cursor" above it
    action.click()                                              #and
    action.perform()                                            #click it

time.sleep(eaTime)                                              #delay to avoid errors

                                                                #all of this repeats until time.sleep(0.1)
if result_list[1] == "1":                                       #with all other faces so I will not comment it
    action.move_to_element_with_offset(element[0], 115, 120)
    action.click()
    action.perform()

time.sleep(eaTime)

if result_list[2] == "1":
    action.move_to_element_with_offset(element[0], 218, 120)
    action.click()
    action.perform()

time.sleep(eaTime)

if result_list[3] == "1":
    action.move_to_element_with_offset(element[0], 40, 204)
    action.click()
    action.perform()

time.sleep(eaTime)

if result_list[4] == "1":
    action.move_to_element_with_offset(element[0], 118, 204)
    action.click()
    action.perform()


time.sleep(eaTime)

if result_list[5] == "1":
    action.move_to_element_with_offset(element[0], 195, 204)
    action.click()
    action.perform()

time.sleep(eaTime)

if result_list[6] == "1":
    action.move_to_element_with_offset(element[0], 44, 280)
    action.click()
    action.perform()

time.sleep(eaTime)

if result_list[7] == "1":
    action.move_to_element_with_offset(element[0], 126, 280)
    action.click()
    action.perform()


time.sleep(eaTime)

if result_list[8] == "1":
    action.move_to_element_with_offset(element[0], 200, 280)
    action.click()
    action.perform()


time.sleep(0.1)                                                   #avoid errors

action.move_to_element_with_offset(element[0], 205, 340)          #move the "cursor" above the box...
action.click()                                                    #and
action.perform()                                                  #click it

os.system("del face_0.png")                                       #remove everything that isn't needed anymore
os.system("del face_1.png")
os.system("del face_2.png")
os.system("del face_3.png")
os.system("del face_4.png")
os.system("del face_5.png")
os.system("del face_6.png")
os.system("del face_7.png")
os.system("del face_8.png")
