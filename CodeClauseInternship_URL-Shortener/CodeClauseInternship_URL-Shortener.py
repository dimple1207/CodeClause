import pyperclip
import pyshorteners
from tkinter import *

root = Tk()

root.title("🚀 URL Magic Shortener 🚀")
root.configure(bg="#49A")

url = StringVar()
url_address = StringVar()

def url_shorten():
    user_url = url.get()
    shortened_url = pyshorteners.Shortener().tinyurl.short(user_url)
    url_address.set(shortened_url)

def copy_url():
    shortened_url = url_address.get()
    pyperclip.copy(shortened_url)

def maximize_window():
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

def minimize_window():
    root.attributes('-zoomed', False)

# Set resizable and maximize/minimize options
root.resizable(True, True)

# Creative GUI design
root.geometry("600x400")

background_label = Label(root, bg="#49A")
background_label.place(relwidth=1, relheight=1)

title_label = Label(root, text="✨ Welcome to the URL Shortener ✨", font=("Arial", 24, "bold"), bg="#49A", fg="white")
title_label.pack(pady=20)

url_entry = Entry(root, textvariable=url, font=("Arial", 14), fg="grey", bd=2, relief=GROOVE)
url_entry.insert(0, "Enter your long URL here")
url_entry.bind("<FocusIn>", lambda event: url_entry.delete(0, "end") and url_entry.config(fg="black"))
url_entry.bind("<FocusOut>", lambda event: url_entry.insert(0, "Enter your long URL here") and url_entry.config(fg="grey"))
url_entry.pack(pady=20, padx=20, fill=X)

shorten_button = Button(root, text="🔗 Generate Short URL", command=url_shorten, bg="#FFD700", fg="black", font=("Arial", 14, "bold"))
shorten_button.pack(pady=15)

copy_button = Button(root, text="📋 Copy Short URL", command=copy_url, bg="#20B2AA", fg="white", font=("Arial", 14, "bold"))
copy_button.pack(pady=10)

short_url_entry = Entry(root, textvariable=url_address, font=("Arial", 14, "italic"), fg="#4169E1", bd=2, relief=GROOVE)
short_url_entry.pack(pady=20, padx=20, fill=X)

# Footer with credit
footer_label = Label(root, text="✨ Created with by Dimple❤️✨", font=("Arial", 12, "italic"), bg="#49A", fg="white")
footer_label.pack(side=BOTTOM, fill=X)

root.mainloop()
