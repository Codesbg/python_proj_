#text editor and notepad

import tkinter as tk
from tkinter import filedialog,messagebox
def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".text",filetypes=[("text file","*.txt")])
    if file_path:
        with open_file(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
        file_path=filedialog.asksaveasfilename(defaultextension=".text",filetypes=[("text files","*.txt")])
        if file_path:
            with open (file_path ,"w")as file:
                file.write(text.get(1.0,tk.END))
                messagebox.showinfo("info","file save sucessfully !")

root=tk.Tk()
root.title("MY NOTEPAD")
root.geometry("800x600")
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command= new_file)
file_menu.add_command(label="Open",command= open_file)
file_menu.add_command(label="Save",command= save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

text=tk.Text(root,wrap=tk.WORD,font=("arial",10), fg="black",bg="white")
text.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()

"""
    - **`filedialog.askopenfilename`**:
    - This is a function from the `tkinter.filedialog` module. It opens a dialog box that allows the user to select a file from their filesystem. Once the user selects a file, the function returns the full path to the selected file as a string. If the user cancels the operation, it returns an empty string.

- **`defaultextension=".text"`**:
    - This specifies the default file extension that will be automatically added if the user doesn't provide one while saving or opening a file.
    - In this case, `.text` is being set as the default extension. However, `.text` isn't a standard text file extension—it should ideally be `.txt`.

- **`filetypes=[("text file", "*.txt")]`**:
    - The `filetypes` argument specifies the types of files the open dialog should display in its file filter.
    - This creates a filter labeled `"text file"` in the file dialog, and only files with the `.txt` extension are shown.
    - `"*.txt"` is a wildcard pattern:
        - `*` matches any file name.
        - `.txt` matches files with the `.txt` extension.

### Overall Meaning of the Line:
1. The line opens a file dialog box where:
    - The user can select files with a `.txt` extension.
    - If the user doesn't specify a file extension, the default extension `.text` is added automatically (although this should ideally be `.txt`).

2. The full path of the selected file is stored in the variable `file_path`. If the user cancels the operation, `file_path` will be an empty string.

In summary, this line allows the user to browse and select a text file (`.txt`) from their system, and it stores the file's path in the `file_path` variable. Let me know if you need further clarification!

### Explanation:
1. **`if file_path:`**
    - Checks if the user has selected a file (i.e., `file_path` is not an empty string).

2. **`with open_file(file_path, "r") as file:`**
    - Opens the file located at the path stored in `file_path` in **read mode** (`"r"`).
    - However, `open_file` here seems incorrectly used; it should likely be `open` instead of `open_file`.

3. **`text.delete(1.0, tk.END)`**
    - Clears all existing text in the `text` widget.
    - `1.0` specifies the starting point (row 1, column 0), and `tk.END` specifies the end of the text widget.

4. **`text.insert(tk.END, file.read())`**
    - Inserts the contents of the opened file into the `text` widget.
    - `file.read()` reads the entire content of the file as a string.

    """


