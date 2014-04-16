from Tkinter import *
import ttk

root = Tk()
root.title("Hello world!")
mainframe = ttk.Frame(root, padding="5  10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
hello = StringVar()
text = StringVar()
hello_entry = ttk.Entry(mainframe, width=50, textvariable=hello)
hello_entry.grid(column=0, row=0, sticky=(N, E))


def print_hello(*args):
    text.set(hello.get())

ttk.Button(mainframe, width=10,
           text="send",
           command=print_hello).grid(column=1, row=0, sticky=(N, E))
hello_label = ttk.Label(mainframe, textvariable=text).grid(column=0,
                                                           row=1,
                                                           sticky=(W, S))
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
hello_entry.focus()
root.bind('<Return>', print_hello)
root.mainloop()
