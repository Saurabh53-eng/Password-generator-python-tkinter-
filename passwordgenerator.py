#importing Libraries
from tkinter import *
import tkinter as tk
import random, string
from tkinter import font
import pyperclip
from PIL import ImageTk, Image
import PIL
import pyperclip as pc
import shutil
root =Tk()

root.geometry("400x400")

root.resizable(0,0)
root.title("PASSWORD GENERATOR")
global selected
selected=False
file="/home/saurabh/Downloads/python-password-generator/giphy (1).gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

gif_label = tk.Label(root,image="")
gif_label.place(x=0,y=0)

#img = PhotoImage(file='/home/saurabh/Downloads/python-password-generator/password.gif', format="gif -index 2")
#
#label = Label(
#    root,
#    image=img,
#    anchor=NW
#)   
#label.place(x=0,y=0)

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
print(animation(count))
###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

#initialize window

pass_str = StringVar()
pass_text=StringVar()

def no():
    password = ''
    for x in range (0,3):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)
    for y in range(pass_len.get()- 3):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    pass_str.set(password)

def yes():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

def et():
    root.destroy()

def printValue():
    pname = player_name.get()
    wip = ''
    for x in range (0,5):
        wip = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)+(pname)
    for y in range(pass_len.get()- 5):
        wip = wip+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation+pname)
    pass_text.set(wip)






Label(root, text = "Want Punctuation",font= 'arial 12 bold').pack(pady=5)

Y=Button(root, text = "YES",width=10,command=yes).pack()
N=Button(root, text = "NO",width=10,command=no).pack()

e=Entry(root , textvariable = pass_str).pack(pady=5)

Label(root, text = 'Want word to add in password',font= 'arial 12 bold').pack(pady=3)

Label(root, text = 'Enter word',font= 'arial 12 bold').pack(pady=5)

def copy_text(e):
    global selected
    if a.selection_get():
        
        selected=a.selection_get()


player_name = Entry(root)
player_name.pack(pady=3)
Button(
    root,
    text="Add word", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

a=Entry(root , textvariable = pass_text)
a.pack()

exit=Button(root,text='EXIT',width=10,command=et).pack()
Label(root, font= 'arial 12 bold', text='(y or n) -->').place(x= 60,y=110)
Button(root,text="CopyPassword", padx=1, pady=5,command=lambda: copy_text(False)).pack()
# loop to run program 
root.mainloop()
