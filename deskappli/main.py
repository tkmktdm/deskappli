import tkinter as tk
import os
from tkinter import messagebox

#input
def button_click():
    input_value = input_box.get()
    output.insert(tk.END,input_value)
    # messagebox.showinfo('クリックイベント',input_value + 'が入力されました。')

#os command
def button_console():
    input_v = input_box.get()
    print(input_v)
    os.system('say '+ input_v)
    
#end
def end_select():
    select=messagebox.askquestion('','本当に終了しますか？')
    if select=='yes':
        root.quit()

#label add
def button_command():
    command = input_box.get()
    print(command)
    oss = os.system(command)
    output.insert(tk.END, oss)

#delete
def button_delete():
    output.delete(0)

# window
root = tk.Tk()
root.title('Python GUI')
root.geometry('720x640')

# input box
input_box = tk.Entry(width=40)
input_box.place(x=100, y=100)

# label
input_box_label = tk.Label(text='box')
input_box_label.place(x=25, y=100)

# output
output = tk.Listbox(width=55, height=15)
output.place(x=100, y=300)

# button
button = tk.Button(text = '実行ボタン', command = button_click)
button.place(x=10, y=150)
button = tk.Button(text = 'sayコマンドボタン', command = button_console)
button.place(x=10, y=200)
button = tk.Button(text = '終了ボタン', command = end_select)
button.place(x=10, y=0)
button = tk.Button(text = 'コマンド操作', command = button_command)
button.place(x=10, y=250)
button = tk.Button(text = '削除', command = button_delete)
button.place(x=50, y=150)

root.mainloop()
