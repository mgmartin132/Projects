import tkinter as tk
from tkinter import font

class Caesar():
    def __init__(self):
        self.LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.translated = ""

    # Defines the encryption function
    def __cipher(self, mode):
        for letter in self.plaintext.upper():
            if letter in self.LETTERS:
                l = self.LETTERS.find(letter)
                
                if mode == "encrypt":
                    l = l + int(self.key)
                elif mode == "decrypt":
                    l = l - int(self.key)

                if l >= len(self.LETTERS):
                    l = l - len(self.LETTERS)
                elif l < 0:
                    l = l + len(self.LETTERS)
                
                self.translated = self.translated + self.LETTERS[l]
            else:
                print("Input contains invalid characters")
                quit()

    # Calls for the program to encrypt a given message
    def encrypt(self, plaintext, key):
        self.translated = ""
        self.key = key
        self.plaintext = plaintext
        self.__cipher("encrypt")
        return self.translated
    
    # Calls for the program to decrypt a given message
    def decrypt(self, plaintext, key):
        self.translated = ""
        self.key = key
        self.plaintext = plaintext
        self.__cipher("decrypt")
        return self.translated

class CaesarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("1200x480")
        
        self.cipher = Caesar()
        self.create_widgets()

    def create_widgets(self):
        default_font = font.Font(family="TKDefaultFont")
        default_font.configure(size=18)

        frame_input = tk.Frame(self.root)
        frame_input.pack(side=tk.TOP, pady=20)

        self.label_key = tk.Label(frame_input, text="Key Value (1-25):")
        self.label_key.pack()
        self.label_key.configure(font="TKDefaultFont")
        self.entry_key = tk.Entry(frame_input, validate="key", validatecommand=(root.register(self.validate_key), "%P"))
        self.entry_key.pack()
        self.entry_key.configure(font="TKDefaultFont", )

        self.label_message = tk.Label(frame_input, text="Message (256 char. max, A-Z only, no whitespace):")
        self.label_message.pack()
        self.label_message.configure(font="TKDefaultFont")
        self.entry_message = tk.Entry(frame_input, validate="key", validatecommand=(root.register(self.validate_message), "%P"))
        self.entry_message.pack()
        self.entry_message.configure(font="TKDefaultFont", width=100)

        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(side=tk.TOP, pady=10)

        self.button_encrypt = tk.Button(frame_buttons, text="Encrypt", command=self.encrypt)
        self.button_encrypt.pack(side=tk.LEFT, padx=15)
        self.button_encrypt.configure(font="TKDefaultFont")
        
        self.button_decrypt = tk.Button(frame_buttons, text="Decrypt", command=self.decrypt)
        self.button_decrypt.pack(side=tk.LEFT, padx=15)
        self.button_decrypt.configure(font="TKDefaultFont")

        frame_result = tk.Frame(self.root)
        frame_result.pack(side=tk.TOP, pady=20)

        self.label_result = tk.Label(frame_result, text="Result:")
        self.label_result.pack()
        self.label_result.configure(font="TKDefaultFont")
        self.text_result = tk.Text(frame_result, height=4, width=100)
        self.text_result.pack()
        self.text_result.configure(font="TKDefaultFont")

    def validate_key(self, value):
        if value == "" or (value.isdigit() and len(value) <= 2):
            return True
        else:
            return False

    def validate_message(self, value):
        if value.isalpha() and len(value) <= 256:
            return True
        else:
            return False

    def encrypt(self):
        key = int(self.entry_key.get())
        message = self.entry_message.get()
        result = self.cipher.encrypt(message, key)
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result)

    def decrypt(self):
        key = int(self.entry_key.get())
        message = self.entry_message.get()
        result = self.cipher.decrypt(message, key)
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarGUI(root)
    root.mainloop()
