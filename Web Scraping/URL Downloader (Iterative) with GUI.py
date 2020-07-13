import tkinter as tk
import ctypes
import urllib.request as req
import os

user32 = ctypes.windll.user32
HEIGHT  = user32.GetSystemMetrics(0)* 0.25 
WIDTH = user32.GetSystemMetrics(1) * 0.4

root = tk.Tk()
root.title("URL Downloader (Iterative)")
root.iconbitmap('SigIcon.ico')

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth = 0.9, relheight = 0.9, relx = 0.05, rely = 0.05)

base_url_lb = tk.Label(frame, text = "Base URL :")
base_url_lb.grid(row = 0, column = 0, sticky = "e")

base_url = tk.Entry(frame)
base_url.grid(row = 0, column = 1)

str_index_lb = tk.Label(frame, text = "Starting index (all digits) :")
str_index_lb.grid(row = 1, column = 0, sticky = "e")

str_index = tk.Entry(frame)
str_index.grid(row = 1, column = 1)

#index = int(str_index)
#needs_onset = False if len(str_index) == len(str(index)) else True

endex_lb = tk.Label(frame, text = "Ending at index : ")
endex_lb.grid(row = 2, column = 0, sticky = "e")

endex = tk.Entry(frame)
endex.grid(row = 2, column = 1)

button = tk.Button(root, text="Download")
button.pack()
		
root.mainloop()