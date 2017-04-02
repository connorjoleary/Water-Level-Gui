import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

import numpy as np
data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
data2 = np.genfromtxt('data1.csv', delimiter=',', names=['date', 'level'])
f = Figure(figsize=(5,5), dpi=100)

Tanks = []

def update(f):
    f.clear()
    a = f.add_subplot(2,2,2)
    data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
    a.plot(data['x'], data['y'], color='r', label='the data')

    a2 = f.add_subplot(2,2,4)
    data2 = np.genfromtxt('data1.csv', delimiter=',', names=['date', 'level'])
    a2.plot(data2['date'], data2['level'], color='r', label='Tank 2')
    f.canvas.draw()

    print ("update")
    main.after(3000, update, f)

class mainP(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphPage, InfoPage):
            frame = F(container, self)
            self.frames[F] = frame
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

        button = ttk.Button(self, text="Graphs",
                            command=lambda: controller.show_frame(GraphPage))
        button.pack()
        button2 = ttk.Button(self, text="Information",
                            command=lambda: controller.show_frame(InfoPage))
        button2.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Information Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="New Tank",
                            command=lambda: add_tank())
        button2.pack()

        #Add one tank
        Tanks.append(add_tank)
        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def add_tank():
        tank = Frame(GraphPage, self)
        a = f.add_subplot(111)
        a.plot(data['x'], data['y'], color='r', label='Tank 1')
        
        # a2 = f.add_subplot(111)
        a.plot(data2['date'], data2['level'], color='r', label='Tank 2')

        return tank


main = mainP()
main.after(3000, update, f)
main.mainloop()
