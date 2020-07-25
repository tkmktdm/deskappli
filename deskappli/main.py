import tkinter as tk
import os
from tkinter import messagebox
from img import Logo
from mysql import connect

import tkinter.ttk as ttk

class NotebookSample(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        note = ttk.Notebook(self)
        note.pack()
        note0 = ttk.Frame(note,width=720,height=640)
        note1 = ttk.Frame(note,width=720,height=640)
        note.add(note0,text="create")
        note.add(note1,text="show")
        #note.add(note0,)




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

#sql
def button_sql():
    name = name_box.get()
    mail = mail_box.get()
    pw = pass_box.get()

    sql = connect()
    cnct,cur,table,status = sql.setting()
    req = sql.insert(name, mail, pw, cnct)
    output.insert(tk.END, req)

# window
root = tk.Tk()
root.title('DeskAppli')
#icon表示させられたらする
#data = Logo.title_logo()
#img = tk.PhotoImage(data=data)
#root.tk.call('vm', 'iconphoto', root._w, tk.PhotoImage(data=data))
root.geometry('720x640')
#root['bg'] = 'blue'

# input box
#input_box = tk.Entry(width=40)
#input_box.place(x=100, y=100)
name_box = tk.Entry(width=40)
name_box.place(x=100, y=150)
mail_box = tk.Entry(width=40)
mail_box.place(x=100, y=200)
pass_box = tk.Entry(width=40)
pass_box.place(x=100, y=250)

# label
input_box_label = tk.Label(text='box')
input_box_label.place(x=25, y=100)
name_label = tk.Label(text='name')
name_label.place(x=25, y=150)
mail_label = tk.Label(text='mail')
mail_label.place(x=25, y=200)
pass_label = tk.Label(text='pass')
pass_label.place(x=25, y=250)

# output
output = tk.Listbox(width=55, height=15)
output.place(x=100, y=350)

# button
#button = tk.Button(text = '実行ボタン', command = button_click)
#button.place(x=10, y=300)
#button = tk.Button(text = 'sayコマンドボタン', command = button_console)
#button.place(x=175, y=300)
button = tk.Button(text = '終了ボタン', command = end_select)
button.place(x=10, y=30)
#button = tk.Button(text = 'コマンド操作', command = button_command)
#button.place(x=320, y=300)
#button = tk.Button(text = '削除', command = button_delete)
#button.place(x=110, y=300)

button = tk.Button(text = 'sql', command = button_sql)
button.place(x=11, y=350)

NotebookSample(root)
root.mainloop()
