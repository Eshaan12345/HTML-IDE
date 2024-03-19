#html runner

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
import os

ide = Tk()
ide.minsize(600,600)
ide.maxsize(600,600)
ide.configure(background = "gray20")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open('exit.jpg'))

file_name_label = Label(ide, text = "File Name : ", bg = "gray20", fg = "snow")
file_name_label.place(relx = 0.55, rely = 0.05, anchor = CENTER)
file_name_entry = Entry(ide, bg = "gray17", fg = "snow")
file_name_entry.place(relx = 0.763, rely = 0.05, anchor = CENTER, width = 175)

code_editor = Text(ide, height = 30, width = 70, bg = "gray17", fg = "snow")
code_editor.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""

def openFile():
    global name
    file_name_entry.delete(0, END) 
    code_editor.delete(1.0, END)
    text = filedialog.askopenfile(title="Open Html file", filetype=(("Html Files", "*.html"),))
    if text:
        name = text.name  # Get the file name
        formatted_name = os.path.basename(name).split(".")[0] 
        file_name_entry.insert(0, formatted_name) 
        content = open(name, 'r')
        main_content = content.read() 
        code_editor.insert(1.0, main_content) 
        content.close()

   
def saveFile():
    input_name = file_name_entry.get()
    file = open(input_name + ".html", "w")
    data = code_editor.get("1.0", END)
    print(data)
    file.write(data)
    file_name_entry.delete(0, END)
    code_editor.delete(1.0, END)
    messagebox.showinfo("Hey friend!", "The contents of the file have been saved successfully.")
    
def runFile():
    html_content = code_editor.get(1.0, END)
    with open('temp.html', 'w') as temp_html_file:
        temp_html_file.write(html_content)
    webbrowser.open_new_tab('temp.html')

open_btn = Button(ide, text = "Open", command = openFile, bg = "gray17", fg = "snow")
open_btn.place(relx = 0.07, rely = 0.05, anchor = CENTER)

save_btn = Button(ide, text = "Save", command = saveFile, bg = "gray17", fg = "snow")
save_btn.place(relx = 0.17, rely = 0.05, anchor = CENTER)

open_btn = Button(ide, text = "Run", command = runFile, bg = "gray17", fg = "snow")
open_btn.place(relx = 0.27, rely = 0.05, anchor = CENTER)

ide.mainloop()