#!/usr/bin/env Python3

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def convert_data():
    # Get the input data from the textbox
    input_data = text_area.get("1.0", "end-1c")

    # Add the '2D' text to the input text
    output_data = input_data.replace("-", "-2D")

    # Display the results in the output textbox
    output_area.delete("1.0", "end")
    output_area.insert("1.0", output_data)

root = tk.Tk()

root.title("Data Slide Conversion")

ttk.Label(root, text="Data Slide Conversion", font=("Times New Roman", 15)).grid(column=0, row=0)
ttk.Label(root, text="Use Ctrl + V to paste in", font=("Bold", 12)).grid(column=0, row=1)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15))
text_area.grid(column=0, row=2, pady=10, padx=10)

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15))
output_area.grid(column=0, row=4, pady=10, padx=10)

ttk.Button(root, text="Convert Data", command=convert_data).grid(column=0, row=3, pady=10)

# placing cursor in text area
text_area.focus()
root.mainloop()