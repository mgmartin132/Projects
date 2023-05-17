# A file validation tool
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import time
import os
import hashlib

file_path1 = ""
file_path2 = ""

file_hash1 = ""
file_hash2 = ""

result_text = ""

def FileHashCompare():
    global result_text
    # Function compares the hash values of two files
    def hash_compare(file_path1, file_path2):     
        global result_text
        if file_hash1 == file_hash2:
            result_text = "Hash match. The files are identical."
        else:
            result_text = "Hash mismatch. The files are different."

    if file_path1 == "" or file_path2 == "":
        result_text = "No file(s) selected."
        return
    else:     
        hash_compare(file_hash1, file_hash2)

# Function performs hash calculation on specified file
def file_hash(file_path):
    hasher = hashlib.sha256() # Function calculates the hash of a file using SHA256 algorithm
    with open(file_path, 'rb') as file: # Opens the file in binary mode
        for chunk in iter(lambda: file.read(4096), b""): # Reads the file in iterations of 4096 byte chunks
            hasher.update(chunk) # Updates the internal state of the hash algorithm for each chunk processed
    return hasher.hexdigest() # Returns the hexadecimal representation of the final hash digest

# Class defining the GUI for the program
class HashCompGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FileHash Compare")
        self.root.geometry("1400x800")
        self.default_font = font.Font(family="Lucida Console", size=14)

        self.create_widgets()
    
    def create_widgets(self):
        frame_header = tk.Frame(self.root, padx=10, pady=10)
        frame_header.pack(side=tk.TOP)

        self.label_header = tk.Label(frame_header, text="Select the files you wish to compare.")
        self.label_header.configure(font=self.default_font)
        self.label_header.grid(row=1, columnspan=2, pady=20)

        self.label_button1 = tk.Label(frame_header, text="File 1")
        self.label_button1.configure(font=self.default_font)
        self.label_button1.grid(row=2, column=0, padx=240, pady=5)

        self.button_browse_file1 = tk.Button(frame_header, text="Browse PC", command=lambda: self.file_browser(1))
        self.button_browse_file1.configure(font=self.default_font)
        self.button_browse_file1.grid(row=3, column=0, padx=240)

        self.label_button2 = tk.Label(frame_header, text="File 2")
        self.label_button2.configure(font=self.default_font)
        self.label_button2.grid(row=2, column=1, padx=240, pady=5)

        self.button_browse_file2 = tk.Button(frame_header, text="Browse PC", command=lambda: self.file_browser(2))
        self.button_browse_file2.configure(font=self.default_font)
        self.button_browse_file2.grid(row=3, column=1, padx=240)

        frame_files = tk.Frame(self.root, padx=10, pady=60)
        frame_files.pack(side=tk.TOP)

        self.label_file1 = tk.Label(frame_files, text="Selected File 1")
        self.label_file1.configure(font=self.default_font)
        self.label_file1.grid(row=1, column=0, padx=200, pady=5)

        self.text_file1 = tk.Text(frame_files, width=50, height=20, bg="black", fg="white")
        self.text_file1.configure(font=self.default_font)
        self.text_file1.grid(row=2, column=0, padx=20)

        self.label_file2 = tk.Label(frame_files, text="Selected File 2")
        self.label_file2.configure(font=self.default_font)
        self.label_file2.grid(row=1, column=1, padx=200, pady=5)

        self.text_file2 = tk.Text(frame_files, width=50, height=20, bg="black", fg="white")
        self.text_file2.configure(font=self.default_font)
        self.text_file2.grid(row=2, column=1, padx=20)

        frame_compare = tk.Frame(self.root, padx=10, pady=20)
        frame_compare.pack(side=tk.TOP)

        self.button_compare = tk.Button(frame_compare, text="COMPARE", command=self.show_results)
        self.button_compare.configure(font=self.default_font)
        self.button_compare.grid(columnspan=2)

    # Function for file browser dialog box and file selection
    def file_browser(self, button_num):
        global file_path1, file_path2, file_hash1, file_hash2
        filename = filedialog.askopenfilename(initialdir=initial_dir, title="Select a File",
                                              filetypes=(("All files", "*.*"),))
        if filename:
            if button_num == 1: # Checks for the button/file currently being specified
                file_path1 = filename # Changes file path variable to the selected file
                if self.text_file1.tag_ranges("sel"):  # Check if there is any selected text in text_file1
                    self.text_file1.delete("sel.first", "sel.last")  # Remove selected text
                self.text_file1.delete("1.0", tk.END)  # Clear the previous file path
                self.text_file1.insert(tk.END, filename)  # Insert file path at the end of the text widget
                file_hash1 = file_hash(file_path1) 
            if button_num == 2:
                file_path2 = filename
                if self.text_file2.tag_ranges("sel"):
                    self.text_file2.delete("sel.first", "sel.last")
                self.text_file2.delete("1.0", tk.END)
                self.text_file2.insert(tk.END, filename)
                file_hash2 = file_hash(file_path2)

    def show_results(self):
        global result_text
        FileHashCompare()
        self.window_compare = tk.Toplevel(self.root)
        self.window_compare.title("Comparison Results")
        self.window_compare.geometry("600x100")

        self.label_result = tk.Label(self.window_compare, text=result_text)
        self.label_result.configure(font=self.default_font)
        self.label_result.pack(padx=10, pady=10)


if __name__ == "__main__":
    # This block handles OS detection in order to decide the inital directory for the file browser
    if os.name == "nt": # Windows
        initial_dir = "C:\\"
    elif os.name == "posix": # Linux
        initial_dir = "/"
    else:
        print("Unknown operating system. Exiting program.")
        quit()
    root = tk.Tk()
    app = HashCompGUI(root)
    root.mainloop()
