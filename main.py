import tkinter as tk
from tkinter import messagebox, simpledialog

class LibraryApp:
    def __init__(self, root):
        self.root = root
        root.title("Library Management System")
        root.geometry("500x400")
        root.resizable(False, False)

        # Book storage (list of dicts)
        self.books = []

        # Title label
        tk.Label(root, text="Library Management System", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=15)

        # Title
        tk.Label(root, text="Title:").grid(row=1, column=0, sticky='e', padx=10, pady=5)
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=1, column=1, columnspan=2, pady=5)

        # Author
        tk.Label(root, text="Author:").grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.author_entry = tk.Entry(root, width=30)
        self.author_entry.grid(row=2, column=1, columnspan=2, pady=5)

        # Year
        tk.Label(root, text="Year:").grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.year_entry = tk.Entry(root, width=30)
        self.year_entry.grid(row=3, column=1, columnspan=2, pady=5)

        # eBook Checkbox and entry
        self.ebook_var = tk.IntVar()
        self.ebook_cb = tk.Checkbutton(root, text="Is eBook?", variable=self.ebook_var, command=self.toggle_ebook_entry)
        self.ebook_cb.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        self.ebook_entry = tk.Entry(root, width=30, state='disabled')
        self.ebook_entry.grid(row=4, column=1, columnspan=2, pady=10)

        # Buttons
        self.add_btn = tk.Button(root, text="Add Book", width=15, command=self.add_book)
        self.add_btn.grid(row=5, column=0, pady=15)

        self.remove_btn = tk.Button(root, text="Remove Selected", width=15, command=self.remove_book)
        self.remove_btn.grid(row=5, column=1, pady=15)

        self.view_btn = tk.Button(root, text="View Books", width=15, command=self.view_books)
        self.view_btn.grid(row=5, column=2, pady=15)

        # Listbox to show books
        self.books_listbox = tk.Listbox(root, width=60, height=10)
        self.books_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def toggle_ebook_entry(self):
        if self.ebook_var.get() == 1:
            self.ebook_entry.config(state='normal')
        else:
            self.ebook_entry.delete(0, tk.END)
            self.ebook_entry.config(state='disabled')

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()
        is_ebook = self.ebook_var.get()
        ebook_data = self.ebook_entry.get().strip()

        if not title or not author or not year:
            messagebox.showerror("Error", "Please fill Title, Author, and Year")
            return

        if is_ebook:
            if not ebook_data or not all(c.isalnum() or c in ('_', '.', '/', ':') for c in ebook_data):
                messagebox.showerror("Error", "Enter a valid eBook filename or URL")
                return
        else:
            ebook_data = None

        # Add to books list
        book = {
            'Title': title,
            'Author': author,
            'Year': year,
            'eBook': ebook_data
        }
        self.books.append(book)
        messagebox.showinfo("Success", f"Book '{title}' added!")
        self.clear_entries()
        self.view_books()

    def remove_book(self):
        selected_idx = self.books_listbox.curselection()
        if not selected_idx:
            messagebox.showwarning("Warning", "Please select a book to remove.")
            return
        idx = selected_idx[0]
        book = self.books.pop(idx)
        messagebox.showinfo("Removed", f"Removed book '{book['Title']}'")
        self.view_books()

    def view_books(self):
        self.books_listbox.delete(0, tk.END)
        for idx, book in enumerate(self.books, 1):
            ebook_status = f" [eBook: {book['eBook']}]" if book['eBook'] else ""
            line = f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}){ebook_status}"
            self.books_listbox.insert(tk.END, line)

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.ebook_entry.delete(0, tk.END)
        self.ebook_entry.config(state='disabled')
        self.ebook_var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
