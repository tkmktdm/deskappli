import tkinter as tk
import os
from tkinter import messagebox
from img import Logo
from mysql import connect
import tkinter.ttk as ttk


class Application(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master, width=720,height=640)
        self.master.title('deskappli')

        tab1 = tk.Frame(self.master)
        self.add(tab1, text="home")
        Tab1(master=tab1)

        tab2 = tk.Frame(self.master)
        self.add(tab2, text="show")
        Tab2(master=tab2)

        self._quit_outside_widget()
        self.pack()

    def _quit_outside_widget(self):
        quit = tk.Button(self.master,
                         text="QUIT at outside",
                         command=root.destroy)
        quit.pack(side=tk.BOTTOM)


class Tab1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._label_tab1_widget()
        self._quit_tab1_widget()
        #self.end_select()
        self.input_tab1()
        self.output_tab1()
        self.pack()

    def _label_tab1_widget(self):
        label = tk.Label(self, text='Hello World at tab1')
        label.pack()

    #def end_select(self):
    #    select=messagebox.askquestion('','本当に終了しますか？')
    #    if select=='yes':
    #        root.quit()
            #if select=='yes':
            #quit.pack()
    def input_tab1(self):
        input_b = tk.Label(text='box')
        input_b.place(x=100, y=100)
        name_box = tk.Entry(width=40)
        name_box.place(x=130, y=100)

    def output_tab1(self):
        output = tk.Listbox(width=55, height=15)
        output.place(x=100, y=200)

    def _quit_tab1_widget(self):
        quit = tk.Button(self,
                         text="終了",
                         command=root.destroy)
        quit.pack(side=tk.BOTTOM)


class Tab2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._start_tab2_widget()
        self._quit_tab2_widget()
        self.pack()

    def _start_tab2_widget(self):
        start_button = tk.Button(self,
                                 text="say hello",
                                 command=self._hello)
        start_button.pack()

    def _quit_tab2_widget(self):
        quit = tk.Button(self,
                         text="QUIT at tab2",
                         command=root.destroy)
        quit.pack()

    def _hello(self):
        print("Hello World at tab2")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
