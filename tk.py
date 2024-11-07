from tkinter import *
from tkinter import ttk

class Amit_ML:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Amit- Machine Learning Diploma")
        self.root.configure(bg="white")

        # Title
        title = Label(self.root, text="Amit-Machine Learning Diploma", font=("time new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Clock label
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=40)

        # Table setup
        self.setup_table()

    def setup_table(self):
        # Create a frame for the table to cover the rest of the window
        table_frame = Frame(self.root)
        table_frame.place(x=0, y=110, relwidth=1, relheight=1)

        # Set Treeview style
        style = ttk.Style()
        style.configure("Treeview", font=("times new roman", 18),rowheight=50, borderwidth=1)
        style.map("Treeview", background=[("selected", "lightblue")])

        # Define columns
        columns = ('#1', '#2')
        self.table = ttk.Treeview(table_frame, columns=columns, show='headings', height=9, style="Treeview")
        self.table.heading('#1', text=' ')
        self.table.heading('#2', text='')

        # Set column widths with borders
        self.table.column('#1', width=10, anchor='center')
        self.table.column('#2', width=400, anchor='center')
        
        rows = [('Linear Regression', '-----'), ("Logistic Regression", '-----')] + [('', '')] * 12
        for i, row in enumerate(rows):
            bg_color = 'lightgrey' if i % 2 == 0 else 'white'
            self.table.insert('', 'end', values=row, tags=('evenrow' if i % 2 == 0 else 'oddrow',))
        # Tag configuration for row colors
        self.table.tag_configure('evenrow', background='lightgrey')
        self.table.tag_configure('oddrow', background='white')

        # Pack the table to fill the frame
        self.table.pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    root = Tk()
    obj = Amit_ML(root)
    root.mainloop()
