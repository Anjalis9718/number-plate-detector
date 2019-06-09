from django.shortcuts import render
import requests
import cv2
import sys
import matplotlib.pyplot as plt
import pytesseract
import random
import re
import xlwt
import number

def button(request):

    return render(request,'home.html')



def output(request):
    def change_char(s, p, r):
        change= s[:p]+r+s[p+1:]
        return change
    cap = cv2.VideoCapture(0)
    length=9;

    while True:
        if cap.isOpened():
            ret, frame = cap.read()
            print(frame)
            print(ret)
        else:
            ret = False

        img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #img1=cv2.imread(frame, cv2.IMREAD_COLOR)
        #config = ('-l eng --oem 1 --psm 3')
        config = ('-l eng tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --oem 0 --psm 11')

        text1 = pytesseract.image_to_string(img1, config=config)
        text=re.sub('[^0-9A-Z]+', '', text1)
    # Print recognized text

        length=len(text)
        if(length==9 or length==10):
            break

    if(text[0]=='0'):
        text=change_char(text,0,'D')
    elif(text[0]=='1'):
        text=change_char(text,0,'I')

    elif(text[0]=='2'):
        text=change_char(text,0,'Z')
    elif(text[0]=='5'):
        text=change_char(text,0,'S')
    elif(text[0]=='8'):
        text=change_char(text,0,'B')
    else:
        text=text
    if(text[1]=='0'):
        text=change_char(text,1,'O')
    elif(text[1]=='1'):
        text=change_char(text,1,'I')
    elif(text[1]=='2'):
        text=change_char(text,1,'Z')
    elif(text[1]=='5'):
        text=change_char(text,1,'S')
    elif(text[1]=='8'):
        text=change_char(text,1,'B')
    else:
        text=text
    if(text[2]=='0'):
        text=change_char(text,2,'O')
    elif(text[2]=='I'):
        text=change_char(text,2,'1')
    elif(text[2]=='Z'):
        text=change_char(text,2,'2')
    elif(text[2]=='S'):
        text=change_char(text,2,'5')
    elif(text[2]=='B'):
        text=change_char(text,2,'8')
    else:
        text=text
    if(text[3]=='D'):
        text=change_char(text,3,'O')
    elif(text[3]=='I'):
        text=change_char(text,3,'1')
    elif(text[3]=='Z'):
        text=change_char(text,3,'2')
    elif(text[3]=='S'):
        text=change_char(text,3,'5')
    elif(text[3]=='B'):
        text=change_char(text,3,'8')
    else:
        text=text
    #plt.imshow(img1)
    #plt.title('Color Image RGB')
    #plt.xticks([])
    #plt.yticks([])
    #plt.show()
    print(text)
    data=text

    cap.release()


    from firebase import firebase
    import datetime

    firebase=firebase.FirebaseApplication('https://parking-data-11955.firebaseio.com')
    num=random.randint(1,10001)
    #result=firebase.post('/',{'Number':data})
    #result=firebase.post('/',{'Time':datetime.datetime.now()})
    #num=number.variables()
    result=firebase.put('/',num,{'number':data,'time':datetime.datetime.now()})
    #result=firebase.put('/','time',datetime.datetime.now())
    print(result)



    return render(request,'home.html',{'data':data})
