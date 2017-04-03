import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk, Listbox, Scrollbar

LARGE_FONT= ("Verdana", 12)

import numpy as np
data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
data2 = np.genfromtxt('data1.csv', delimiter=',', names=['date', 'level'])

tanks = []

def update(tanks):
    for tank in tanks:
        tank.f.clear()
        a = tank.f.add_subplot(2,2,2)
        data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
        a.plot(data['x'], data['y'], color='r', label='the data')

        a2 = tank.f.add_subplot(2,2,4)
        data2 = np.genfromtxt('data1.csv', delimiter=',', names=['date', 'level'])
        a2.plot(data2['date'], data2['level'], color='r', label='Tank 2')
        tank.f.canvas.draw()

    print ("update")
    main.after(3000, update, tanks)

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
        label.grid(row=0, column=1)
        #self.tanks=[]
        self.num=0

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column = 0)

        button2 = ttk.Button(self, text="New Tank",
                            command=lambda: tanks.append(self.add_tank()))
        button2.grid(row=1, column=2)

        #Add initial tank
        tanks.append(self.add_tank())

        # canvas = FigureCanvasTkAgg(tanks[0].f, self)
        # canvas.show()
        # canvas.get_tk_widget().grid(row=2, column=0)

        # canvas._tkcanvas.grid(row=2, column=1)

    def add_tank(self):
        self.num+=1
        #TODO: correct filename
        fileName = "data"+str(len(tanks))
        print (fileName)

        container = tk.Frame(self)

        frame = TankFrame(container, self, fileName)

        canvas = FigureCanvasTkAgg(frame.f, self)
        canvas.show()
        canvas.get_tk_widget().grid(row=self.num+2, column=0)

        canvas._tkcanvas.grid(row=self.num+2, column=1)
        return frame

class TankFrame(tk.Frame):

    def __init__(self, parent, controller, fileName):
        tk.Frame.__init__(self, parent)
        self.f = Figure(figsize=(5,5), dpi=100)

        #tank = tk.Frame(self)
        a = self.f.add_subplot(111)
        a.plot(data['x'], data['y'], color='r', label='Water Level')
        
        # a2 = f.add_subplot(111)
        a.plot(data2['date'], data2['level'], color='r', label='Info')

        #frame.grid(row=0, column=0, sticky="nsew")

main = mainP()
#main.after(3000, update, tanks)
main.mainloop()
