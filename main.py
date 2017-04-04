import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
#from tkinter import ttk

from buttons import *
import os
import numpy as np
# data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
# data2 = np.genfromtxt('
# data1.csv', delimiter=',', names=['date', 'level'])
figs = [Figure(figsize=(8,3), dpi=100), Figure(figsize=(8,3), dpi=100)]
if not os.path.exists('./values.txt'):
    file = open('values.txt', 'w')
    i=0
    for f in figs:
        i+=1
        file.write("Tank "+str(i)+"\n")
        file.write(str(.26)+"\n")
        file.write(str(.025)+"\n")

def update(f):
    for f in figs:
        f.clear()
        a = f.add_subplot(1,2,1)
        data = np.genfromtxt('data1.csv', delimiter=',', names=['time', 'level'])
        dayData = data[-5:]

        a.plot(dayData['time'], dayData['level'], color='g', label='One Day')
        a.set_title('One Day')
        a.set_ylim(ymin=0)

        a2 = f.add_subplot(1,2,2)
        a2.plot(data['time'], data['level'], color='g', label='One Week')
        a2.set_title('One Week')
        a2.set_ylim(ymin=0)
        f.canvas.draw()

    print ("update")
    main.after(5000, update, figs)

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
        label = tk.Label(self, text="Start Page", font=("Helvetica", 32))
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Graphs",
                            command=lambda: controller.show_frame(GraphPage))
        button.pack()
        button2 = tk.Button(self, text="Settings",
                            command=lambda: controller.show_frame(SettingsPage))
        button2.pack()
        button3 = tk.Button(self, text="Information",
                            command=lambda: controller.show_frame(InfoPage))
        button3.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Information", font=("Helvetica", 32))
        label.grid(row=0, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid()


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
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

        button = tk.Button(self, text="Enter",
                            command=lambda: getValues())
        button.grid(column=2)

        button1 = tk.Button(self, text="Back to Home",  height = 2, width = 14,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(columnspan=3)



class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=("Helvetica", 32))
        label.grid(columnspan=2,pady=10,padx=10)
        i=0
        file = open('values.txt', 'r')
        data = file.readlines()
        for f in figs:
            tk.Button(self, text=data[i*3].replace('\n',''), height = 1, width = 10, borderwidth=1, font=("Helvetica", 20),
                            command=lambda i=i: tank_rename(i)).grid(row=i*3+1,column=0,padx=10)
            
            tk.Label(self, text="Battery Level: "+str(45)+"%", font=("Helvetica", 16)).grid(row=i*3+2,column=0,padx=10)

            tk.Button(self, text="Conversion Factors\nWater:"+data[i*3+1].replace('\n','')+" Battery:"+data[i*3+2].replace('\n',''), 
                            height = 2, width = 18, borderwidth=1, font=("Helvetica", 12),
                            command=lambda i=i: conv_factors(i)).grid(row=i*3+3,column=0,padx=10)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            #canvas.get_tk_widget().grid(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.grid(row=i*3+1,column=1, rowspan=3)

            i+=1

        button1 = tk.Button(self, text="Back to Home", height = 2, width = 14,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(columnspan=2)

main = mainP()
main.after(1, update, figs)
main.mainloop()
