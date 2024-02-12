import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import numpy as np

def grayLevel(image, size, method):
    levels = int(np.log2(size))
    output = np.zeros_like(image, dtype=np.uint8)
    for i in range(levels):
        mask = 2 ** (8 - (i + 1)) - 1
        if method == "low":
            result = (image & ~mask)
        elif method == "middle":
            if i % 2 == 0:
                result = (image & ~mask)
            else:
                result = (image | mask)
        elif method == "high":
            result = (image | mask)
        output = np.maximum(output, result)
    return output

def imageFromFile():
    global output_image
    image_path = path.get()
    image = Image.open(image_path).convert('L')
    image_np = np.array(image)
    size = int(inputSize.get())
    method = inputMethod.get()
    output_image = grayLevel(image_np, size, method)
    output = Image.fromarray(output_image)
    output_image_tk = ImageTk.PhotoImage(image=output)
    imageLabel.config(image=output_image_tk)
    imageLabel.image = output_image_tk

def Open():
    path.set(filedialog.askopenfilename())
        
root = tk.Tk()
root.title("Gray Level Quantization")
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

path = tk.StringVar()
file_label = ttk.Label(frame, text="Select an image:")
file_label.pack()
inputFile = ttk.Entry(frame, textvariable=path)
inputFile.pack()
browse = ttk.Button(frame, text="Browse", command=Open)
browse.pack()
sizeLabel = ttk.Label(frame, text="Quantization Size (2, 4, 8, 16, 32, 64, 128):")
sizeLabel.pack()
inputSize = ttk.Entry(frame)
inputSize.pack()
methodLabel = ttk.Label(frame, text="Quantization Method:")
methodLabel.pack()
inputMethod = ttk.Entry(frame)
inputMethod.pack()
submit = ttk.Button(frame, text="Submit", command=imageFromFile)
submit.pack()
imageLabel = ttk.Label(root)
imageLabel.pack()
root.mainloop()
