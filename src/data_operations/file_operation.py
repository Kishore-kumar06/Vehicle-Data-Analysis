import tkinter as tk
from tkinter.filedialog import askopenfilename



def select_file():
    try:
        root = tk.Tk()
        root.withdraw()
        filepath = askopenfilename()

        return filepath
    except FileNotFoundError as er:
        print(f"An error occured while selecting the file. {er}")
    finally:
        root.destroy()


