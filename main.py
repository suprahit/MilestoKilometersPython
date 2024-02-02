import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


# functions
def convert():
    # print(entry.get())
    # print(entry_int.get())
    mile_input = entry_int.get()
    km_output = mile_input * 1.60934
    output_string.set('{} Km'.format(km_output))


# window
# window = tk.Tk()
window = ttk.Window(themename='darkly')
window.title('Miles to Kilometers Converter')
window.geometry('')
window.config(padx=15, pady=10)

# title
title_label = ttk.Label(master=window, text='Miles to Kilometers Converter', font='Arial 20 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Arial 20', textvariable=output_string)
output_label.pack()

# run
window.mainloop()
