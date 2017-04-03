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
    main.after(5000, update, f)

class mainP(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphPage, SettingsPage, InfoPage):
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
        button2 = ttk.Button(self, text="Settings",
                            command=lambda: controller.show_frame(SettingsPage))
        button2.pack()
        button3 = ttk.Button(self, text="Information",
                            command=lambda: controller.show_frame(InfoPage))
        button3.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Information", font=LARGE_FONT)
        label.grid(row=0, column=1)


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        self.values=["Tank 1", "Tank 2", .26, .025, 7]
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Settings", font=("Helvetica", 32))
        label.grid(row=0, column=0, columnspan=3)

        tk.Label(self, text="Tank Names", font=("Helvetica", 20)).grid(padx=10,row=2,)
        tk.Label(self, text="First",font=("Helvetica", 16)).grid(padx=10,row=2, column=1)
        tk.Label(self, text="Second",font=("Helvetica", 16)).grid(padx=10,row=3, column=1)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e1.grid(padx=10,row=2, column=2)
        e2.grid(padx=10,row=3, column=2)

        tk.Label(self, text="Conversion Factors", font=("Helvetica", 20)).grid(padx=10,row=4)
        tk.Label(self, text="Water Level \n(to get inches)",font=("Helvetica", 16)).grid(padx=10,row=4, column=1)
        tk.Label(self, text="Battery \n(to get volts)",font=("Helvetica", 16)).grid(padx=10,row=5, column=1)

        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e3.grid(padx=10,row=4, column=2)
        e4.grid(padx=10,row=5, column=2)

        tk.Label(self, text="Serial Port Number", font=("Helvetica", 20)).grid(padx=10,row=6)
        e5 = tk.Entry(self)
        e5.grid(padx=10,row=6, column=2)

        button = ttk.Button(self, text="Enter",
                            command=lambda: getValues())
        button.grid()

        def getValues():
            print ("getting Vals")
            self.values=[e1,e2,e3,e4,e5]


class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

main = mainP()
main.after(1, update, f)
main.mainloop()
