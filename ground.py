import tkinter as tk
import numpy as np
import time
import functools

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

main = tk.Tk()
container = tk.Frame(main)
container.pack(side="top", fill="both", expand = True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=main)
canvas.show()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
a.clear()
a.plot(data['x'], data['y'], color='r', label='the data')
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def update(f):
    f.clear()
    a = f.add_subplot(111)
    data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
    a.plot(data['x'], data['y'], color='r', label='the data')
    f.canvas.draw()

    print ("update")
    main.after(3000, update, f)

main.after(3000, update, f)
main.mainloop()