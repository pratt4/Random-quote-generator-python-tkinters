from tkinter import *    
from threading import *   
from PIL import Image,ImageTk   #used to load jpg images
import pygame
import requests


#DEFINING VARIABLES
api = " https://api.quotable.io/random"
quotes = []
quote_number = 0



# for music

pygame.mixer.init()
  #button commands
def play():
    pygame.mixer.music.load('E:/project 1/music.mp3')
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()


# GUI WINDOW

window = Tk()
window.title("QUOTE GENERATOR")
window.geometry("1180x250")


# PRELOADING

def preload_quotes():
    global quotes

    print("***loading more quotes***")
    for x in range(50):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]

        quote =content+"\n\n"+"By \n"+ author
        print(content)



        quotes.append(quote)


    print("***finished loading quotes***")


preload_quotes()    

#BUTTON COMMAND

def get_random_quotes():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number+=1
    print(quote_number)

# THREADING
    if quotes[quote_number]==quotes[-3]:
        thread=Thread(target=preload_quotes)
        thread.start()




# UI

load=Image.open('E:/project 1/bg.jpg')
render=ImageTk.PhotoImage(load)
bgimage=Label(window,image=render)
bgimage.grid(row=0,column=0)

   # header text
textimage=PhotoImage(file='E:/project 1/text.png')
textlabel=Label(window,image=textimage,bd=0,bg='#fcf2e9')
textlabel.place(x=350,y=20)

    #LABEL

quote_label=Label(window,text=' click on the sound button for music ',
                  height=6,              
                  pady=10,
                  wrap=600,
                  bg='#fcf2e9',
                  font=('helvativa',13)
                  ) 
quote_label.grid(row=0,column=0,stick="WE",padx=300,pady=10)

# MUSIC BUTTONS

#play button
playimage=PhotoImage(file="E:/project 1/On1.png")
musicbuttonstart= Button(window,image=playimage,bd=0,command=play,bg='#fcf2e9')
musicbuttonstart.place(x=170,y=130)

#stop button
stopimage=PhotoImage(file="E:/project 1/mute.png")
musicbuttonstop=Button(window,image=stopimage,bd=0,command=stop,bg="#fcf2e9")
musicbuttonstop.place(x=210,y=130)

#GENERATE BUTTON
buttonimage=PhotoImage(file='E:/project 1/generatebutton.png')
button=Button(window,image=buttonimage,command=get_random_quotes,bd=0, bg='#fcf2e9',activebackground='#fcf2e9')
button.place(x=540,y= 200)


window.mainloop()


