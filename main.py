import tkinter as tk
from tkinter import ttk

def toggle_ebook():
    if ebook_var.get():
        ebook_entry.config(state='normal')
    else:
        ebook_entry.config(state='disabled')
        ebook_entry.delete(0, tk.END)

root = tk.Tk()

ebook_var = tk.IntVar()
ebook_checkbox = ttk.Checkbutton(root, text="eBook", variable=ebook_var, command=toggle_ebook)
ebook_checkbox.grid(row=0, column=0, padx=10, pady=10)

ebook_entry = ttk.Entry(root, state='disabled')
ebook_entry.grid(row=0, column=1, padx=10, pady=10)

# To restrict ebook_entry to numbers only, you can use validation
def validate_number(P):
    if P == "" or P.isdigit():
        return True
    return False

vcmd = (root.register(validate_number), '%P')
ebook_entry.config(validate='key', validatecommand=vcmd)

root.mainloop()
