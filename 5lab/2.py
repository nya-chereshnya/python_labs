import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import ctypes
from ctypes import *
from math import log


class CalcApp:
    def __init__(self, master):
        self.master = master
        master.title("My Application")

        self.label_1x = tk.Label(master, text="1x: ")
        self.label_1x.grid(row=0, column=0)
        self.entry_1x = tk.Entry(master)
        self.entry_1x.grid(row=0, column=1)

        self.label_2x = tk.Label(master, text="2x: ")
        self.label_2x.grid(row=1, column=0)
        self.entry_2x = tk.Entry(master)
        self.entry_2x.grid(row=1, column=1)

        self.label_dx = tk.Label(master, text="dx: ")
        self.label_dx.grid(row=2, column=0)
        self.entry_dx = tk.Entry(master)
        self.entry_dx.grid(row=2, column=1)

        self.label_E = tk.Label(master, text="E: ")
        self.label_E.grid(row=3, column=0)
        self.entry_E = tk.Entry(master)
        self.entry_E.grid(row=3, column=1)

        self.button = tk.Button(
            master, text="calculate", command=self.calculate)
        self.button.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        x1 = self.entry_1x.get()
        x2 = self.entry_2x.get()
        dx = self.entry_dx.get()
        E = self.entry_E.get()

        if x1 == "" or x2 == "" or dx == "" or E == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return 0

        x1 = int(x1)
        x2 = int(x2)
        dx = int(dx)
        E = float(E)
        new_window = tk.Toplevel(self.master)
        new_window.title("Таблица")
        columns = ['x', 'result', 'math', 'delta', 'n']
        treeview = ttk.Treeview(new_window, columns=columns, show='headings')

        for col in columns:
            treeview.heading(col, text=col)

        f = cdll.LoadLibrary('./lib.so')
        f.taylor_ln_function.restype = ctypes.POINTER(
            ctypes.POINTER(ctypes.c_double))
        f.taylor_ln_function.argtypes = [
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double]

        result_ptr = f.taylor_ln_function(x1, x2, dx, E)
        result_arr = [[result_ptr[i][j]
                       for j in range(3)] for i in range((x2-x1)//dx)]

        for row in result_arr:
            x = row[0]
            mathValue = log((x + 1) / x)
            n = row[2]
            treeview.insert(
                '', 'end', values=row[0:2] + [mathValue, mathValue - row[1],  int(n)])

        treeview.pack()


root = tk.Tk()
myApp = CalcApp(root)
root.mainloop()
