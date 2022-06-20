# ahegao-captcha-solver

This is a project which is using machine learning to solve Brutalgamerlp's(github.com/Brutalgamerlp) ahegao-captcha(captcha.ahegao.li).
The model was created teachablemachine(teachablemachine.withgoogle.com) and trained with automatically scraped images from the actual captcha.

It might happen that Brutalgamerlp changes the captcha somehow to make it harder to solve automatically but right now(20.6.2022) it had solved 10/10 runs perfectly.

I will keep working on this if im bored and got some time.

Also: a big thanks to the discord user "Chill" from the discord server "Hello World!" he helped me a lot with the problems i had while programming this.

And if you're asking yourself: why?
Simple: I was bored, a friend said its not possible with selenium(proved him wrong) and it definetly was good practice.



# requirements
tensorflow
keras
numpy
cv2 (opencv-python)
selenium
pillow

And a Windows Computer (maybe linux support soon)



# how do i use this?

1. open main.py in your favorite editor or IDE
2. go to driver = webdriver.Firefox()
3. change "Firefox()" to your browser (options: ie, chrome, edge, firefox and opera    NOTE: I only tested Firefox so far)
4. run main.py (tensegao.py gets started automatically once its needed)



# how does it work?

the code is commented quite a bit so just read the comments but here a quick explaination:
1. the URL gets opened
2. the box to start the captcha gets clicked
3. all faces are screenshoted and croped into single files
4. tensegao.py gets started
5. the faces get checked by tensegao.py for ahegaos
6. tensegao.py saves the results to a file
7. tensegao.py ends
8. the results are read by main.py 
9. main.py clicks all ahegao faces in the browser and then the next button


# Q: isnt't the code quite unoptimized?
A: yes, and maybe i'll rewrite it someday but i'm not sure yet
