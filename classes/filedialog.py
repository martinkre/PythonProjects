import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes={("Database", ".db")}, initialfile="pydb1.db")
    return file_path

def open_file():
    try:
        
        
        file_path = filedialog.askopenfile(filetypes={("Database", ".db")}, initialfile="pydb1.db").name
        
            
        return file_path
    except AttributeError as err:
        print(err.args)