# Pre-requisites to import qrcode package by cmd
# Author-Dhruv
import qrcode
from tkinter import *
import os

cp = Tk()
cp.title('generateqr.com')
cp.geometry('700x250')
cp.config(bg='#e52165')

def generate():
    img = qrcode.make(msg.get())
    filename = f'{save_name.get()}.png'
    img.save(filename)

    # to get the path of the file saved
    full_path = os.path.abspath(filename)

    Label(cp, text=f'File Saved at: {full_path}', bg='#e52165',
          fg='black', font=('Arial Black', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    img.show()

frame = Frame(cp, bg='#e52165')
frame.pack(expand=True)

#Entering the text to be converted 
Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='#e52165').grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

#Enter the desired file name
Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='#e52165').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

#Buttons for displaying and saving
btn = Button(cp, text='Save QR code', command=generate, bd='5', width=15)
btn.pack()

btn2 = Button(cp, text='Display QR code', command=show, bd='5', width=15)
btn2.pack()

cp.mainloop()