from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")

txt = Text(window, fg='purple', bg='light yellow', font='Calibri 14')
txt.pack()

current_file = None

def new_file():
    global current_file
    current_file = None
    window.title("Text Editor - Untitled")
    txt.delete("1.0", END)

def open_file():
    global current_file
    filepath = askopenfilename(filetypes=[("Text file", ".txt"), ("All Files", ".*")])
    if not filepath:
        return
    current_file = filepath
    txt.delete("1.0", END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt.insert(END, text)
        window.title(f'Text Editor - {filepath}')

def save_file():
    global current_file
    if current_file:
        filepath = current_file
    else:
        filepath = asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if not filepath:
            return
        current_file = filepath
        window.title(f'Text Editor - {filepath}')

    with open(filepath, mode='w', encoding='utf-8') as output_file:
        text = txt.get('1.0', END)
        output_file.write(text)
        window.title(f'Text Editor - {filepath}')

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_command(label='Save As...', command=save_file)

window.mainloop()