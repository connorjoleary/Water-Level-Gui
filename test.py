import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import time
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

import numpy as np
data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
#needs to be changed
# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)

#start page
class start(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        graphsTk = graphs()
        graphs.after(4000,update)
        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: graphsTk.mainloop())
        button.pack()

class graphs(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = GraphPage(container, self)

        self.frames[GraphPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        # button1 = ttk.Button(self, text="Back to Home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot(data['x'], data['y'], color='r', label='the data')
        print ("upd")


        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    

app = start()
print ("up")
sys.stdout.flush()
print ("down")

# def update(self):
#         data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
#         a.clear()
#         a.plot(data['x'], data['y'], color='r', label='the data')
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         print ("update")
#         sys.stdout.flush()
#         self.after(4000,self.update)


app.mainloop()