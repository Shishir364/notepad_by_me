from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# creating function for commands

def new_File():
    global file 
    root.title("untitled - notepad")
    file = None
    TextArea.delete(1.0 , END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")

def save():
    f = open(file, "w")
    f.write(TextArea.get(1.0, END))
    f.close()
    root.title(os.path.basename(file) + " - Notepad")
    

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
def zoom_in():
    pass
def About():
    showinfo("About","Notepad By Shishir")

""""===============================root created============================================="""

root = Tk()
root.geometry("500x500")
root.title("untitled - notepad")
# root.wm_iconbitmap("notepadicon.ico")
# root.wm_iconbitmap('notepadicon.ico')

"""==============================# File menu strted========================================="""

main_menu = Menu(root)
menu_1 = Menu(main_menu,tearoff=0)
menu_1.add_command(label="New",command=new_File)   # new file creation
# menu_1.add_command(label="New Window",command=new_File)
menu_1.add_command(label="Open",command=openFile)
menu_1.add_command(label="Save",command=save)
menu_1.add_command(label="Save As",command=saveFile)
# this is for line saprater
menu_1.add_separator()
menu_1.add_command(label="Page SetUp",command=new_File)
menu_1.add_command(label="print",command=new_File)
menu_1.add_separator()
menu_1.add_command(label="Exit",command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="File",menu=menu_1)



"""========================# file menu ended======================# EDIT menu strted============================="""


menu_2 = Menu(main_menu,tearoff=0)
menu_2.add_command(label="Undo",command=new_File)
menu_2.add_separator()   # this is for line saprater
menu_2.add_command(label="Cut",command=cut)
menu_2.add_command(label="Copy",command=copy)
menu_2.add_command(label="Paste",command=paste)
menu_2.add_separator()  # this is for line saprater
menu_2.add_command(label="Font",command=quit)

root.config(menu=main_menu)
main_menu.add_cascade(label="Edit",menu=menu_2)

"""==================================# Edit menu ended================# View menu strted===================================="""

menu_3 = Menu(main_menu,tearoff=0)
menu_3.add_command(label="About",command=About)
root.config(menu=main_menu)
main_menu.add_cascade(label="View",menu=menu_3)

"""================# View menu ended======================# Text Area cration ======================="""
 
TextArea = Text(root,font="newtimeroman 20 ")
TextArea.pack(expand=True,fill=BOTH)
file = None

"""================================== #set Scroll Bar on TextArea========================================="""

scroll = Scrollbar(TextArea)
scroll.pack(side= RIGHT , fill=Y ,)
scroll.config(command = TextArea.yview)
TextArea.config(yscrollcommand= scroll.set)

"""===============================================# status bar create in bottom========================================="""
frame = Frame(root)
frame.pack(side=BOTTOM ,fill=X)
l1 = Label(frame,text="python", anchor="e",bg="light gray")
l1.pack(side=BOTTOM ,fill=X)

root.mainloop()