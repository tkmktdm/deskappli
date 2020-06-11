import tkinter as tk
import os
from tkinter import messagebox

def button_click():
    input_value=input_box.get()
    messagebox.showinfo('クリックイベント',input_value + 'が入力されました。')
def button_console():
    input_v=input_box.get()
    print(input_v)
    os.system('say '+ input_v)

#window
root = tk.Tk()
root.title('Python GUI')
root.geometry('500x500')
#input box
input_box = tk.Entry(width=40)
input_box.place(x=100,y=100)
#label
input_box_label=tk.Label(text='box')
input_box_label.place(x=25,y=100)
#button
button=tk.Button(text='実行ボタン',command=button_click)
button.place(x=10,y=130)
button=tk.Button(text='sayコマンドボタン',command=button_console)
button.place(x=10,y=250)

root.mainloop()
