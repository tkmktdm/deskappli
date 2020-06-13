import tkinter as tk
import os
from tkinter import messagebox

def button_click():
    input_value=input_box.get()
    output.insert(tk.END,input_value)
    #messagebox.showinfo('クリックイベント',input_value + 'が入力されました。')
def button_console():
    input_v=input_box.get()
    print(input_v)
    os.system('say '+ input_v)
def end_select():
    select=messagebox.askquestion('','本当に終了しますか？')
    if select=='yes':
        root.quit()

#window
root = tk.Tk()
root.title('Python GUI')
root.geometry('720x640')

#input box
input_box = tk.Entry(width=40)
input_box.place(x=100,y=100)

#label
input_box_label=tk.Label(text='box')
input_box_label.place(x=25,y=100)

#output
output=tk.Listbox(width=55,height=15)
output.place(x=100,y=300)

#button
button=tk.Button(text='実行ボタン',command=button_click)
button.place(x=10,y=150)
button=tk.Button(text='sayコマンドボタン',command=button_console)
button.place(x=10,y=200)
button=tk.Button(text='終了ボタン',command=end_select)
button.place(x=10,y=0)
root.mainloop()
