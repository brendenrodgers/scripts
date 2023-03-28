#!/usr/bin/env Python3

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def convert_data():
    # Get the input data from the textbox
    input_data = text_area.get("1.0", "end-1c")

    # Check if "RC" or "rc" is present in the input data
    if "RC" not in input_data and "rc" not in input_data:
        output_area.delete("1.0", "end")
        output_area.insert("1.0", "Error: Input data must contain 'RC' or 'rc'")
        return

    # Convert all occurrences of "rc" to "RC"
    input_data = input_data.replace("rc", "RC")

    # Split input data by "RC" and join with "\nRC"
    input_data = "\nRC".join(input_data.split("RC")[1:])
    input_data = "RC" + input_data

    # Add the '2D' text to the input text
    output_data = input_data.replace("-", "-2D")

    # Display the results in the output textbox
    output_area.delete("1.0", "end")
    output_area.insert("1.0", output_data)

# Function to clear input text
def clear_input():
    text_area.delete("1.0", "end")
# Function to clear output text
def clear_output():
    output_area.delete("1.0", "end")

root = tk.Tk()

root.title("Data Slide Conversion")

ttk.Label(root, text="Data Slide Conversion", font=("Times New Roman", 15)).grid(column=0, row=0)
ttk.Label(root, text="Use Ctrl + V to paste input", font=("Bold", 12)).grid(column=0, row=1)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15))
text_area.grid(column=0, row=2, pady=10, padx=10)

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15))
output_area.grid(column=0, row=4, pady=10, padx=10)

ttk.Button(root, text="Convert Data", command=convert_data).grid(column=0, row=3, pady=10)
ttk.Button(root, text="Clear Input", command=clear_input).grid(column=1, row=2, pady=10)
ttk.Button(root, text="Clear Output", command=clear_output).grid(column=1, row=4, pady=10)
# placing cursor in text area
text_area.focus()
root.mainloop()