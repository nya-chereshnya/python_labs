import tkinter as tk
import tkinter.ttk as ttk


class Matrix:
    def __init__(self, master) -> None:
        self.master = master

        master.title("Create Matrix")

        self.label_n = tk.Label(master, text="Number of rows (n):")
        self.label_n.grid(row=0, column=0)
        self.entry_n = tk.Entry(master)
        self.entry_n.grid(row=0, column=1)

        self.label_m = tk.Label(master, text="Number of columns (m):")
        self.label_m.grid(row=1, column=0)
        self.entry_m = tk.Entry(master)
        self.entry_m.grid(row=1, column=1)

        self.button_show = tk.Button(master, text="Show Matrix", command=self.show_matrix)
        self.button_show.grid(row=2, column=0)

    def show_matrix(self):
        n = int(self.entry_n.get())
        m = int(self.entry_m.get())
        matrix = self.create_matrix(n, m)
        self.display_matrix(matrix)

    def create_matrix(self, n, m):
        matrix = [[i*j for j in range(m)] for i in range(n)]
        return matrix

    def display_matrix(self, matrix):
        new_window = tk.Toplevel(self.master)
        new_window.title("Matrix")
        columns = ['' for i in range(len(matrix[0]))]
        matrix_table = ttk.Treeview(new_window, columns=columns)
        for col in columns:
            matrix_table.heading(col, text=col)
        for row in matrix:
            matrix_table.insert('', 'end', values=row)
        for i in range(len(columns) + 1):
            matrix_table.column(f'#{i}', width=50, stretch=False)
        matrix_table.column(f'#0', width=0, stretch=False)
        matrix_table.pack()


root = tk.Tk()
my_app = Matrix(root)
root.mainloop()

