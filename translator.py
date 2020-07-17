import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Translator by prince")
win.geometry("500x200")

def tran():
    word = entry.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation1 = translator.translate(word,dest="gu")
    label1 = tk.Label(win,text=f"Translated In Gujarati: {translation1.text}",bg="white")
    label1.grid(row=2,column=0)

label = tk.Label(win,text="Enter Word :")
label.grid(row=0,column=0,sticky="W")

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button= tk.Button(win,text="Translate",command=tran)
button.grid(row=1,column=2)

win.mainloop()