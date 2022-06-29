from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

window = Tk()

# Upload button
def showimage():
    filetypes = (
        ('GIF File', '*.gif'),
        ('All files', '*.*')
    )
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=filetypes)
    img = Image.open(fln)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img

# add text
def add_text():
    global img
    filetypes = (
        ('GIF File', '*.gif'),
        ('All files', '*.*')
    )
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=filetypes)
    img = Image.open(fln)
    text_font = ImageFont.truetype("arial.ttf", 20)
    text_to_add = str(text.get())
    edit_image = ImageDraw.Draw(img)
    edit_image.text((200, 300), text_to_add, ("white"), font=text_font)
    img.save(fln)
        # Clear the entry box
    text.delete(0, END)
    text.insert(0, "Saving File....")
        # Timer
    label.after(2000, show_pic)

def show_pic():
    global photo
    filetypes = (
        ('GIF File', '*.gif'),
        ('All files', '*.*')
    )
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=filetypes)
    photo = PhotoImage(file=fln)
    label.configure(image=photo)
    label.image = photo
    text.delete(0, END)


frame = Frame(window)
frame.pack(side=BOTTOM, padx=15, pady=15)

label = Label(window)
label.pack()

btn = Button(frame, text="Browse Image", command=showimage)
btn.pack(side=LEFT)

btn2 = Button(frame, text="Exit", command=exit)
btn2.pack(side=LEFT, padx=10)

add_text_button = Button(frame, text="add text", command=add_text)
add_text_button.pack(side=LEFT, padx=10)

text = Entry(frame)
text.pack(side=LEFT, padx=10)


window.geometry("400x300")  # Size of the window
window.title('Watermark App')
# Keep the window open
window.mainloop()