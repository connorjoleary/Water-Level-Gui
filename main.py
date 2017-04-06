import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
#from tkinter import ttk

#from buttons import *
import os
import numpy as np
# data = np.genfromtxt('test.csv', delimiter=',', names=['x', 'y'])
# data2 = np.genfromtxt('
# data1.csv', delimiter=',', names=['date', 'level'])
figs = [Figure(figsize=(8,3), dpi=100), Figure(figsize=(8,3), dpi=100)]
file = open('values.txt', 'r')
data = file.readlines()
file.close()
if len(data) <= 0:
    i=0
    for f in figs:
        i+=1
        data.append("Tank "+str(i)+"\n")
        data.append(str(.26)+"\n")
        data.append(str(.025)+"\n")

    file = open('values.txt', 'w')
    file.writelines(data)
    file.close()

def update(f):
    i=0
    for f in figs:
        f.clear()
        a = f.add_subplot(1,2,1)
        weekData = np.genfromtxt('tank3.csv', delimiter=',', dtype="S19, i4, i4")#, names=['time', 'battery', 'level', 'pointer'])
        j=0
        for date in weekData[0]:
            weekData[0][j]= weekData[0][j][11:]
        dayData = weekData[-5:] #TODO: fix with pointer

        a.plot(dayData[0], dayData[2], color='g', label='One Day')
        a.set_title('One Day')
        a.set_ylim(ymin=0)

        a2 = f.add_subplot(1,2,2)
        a2.plot(weekData[0], weekData[2], color='g', label='One Week')
        a2.set_title('One Week')
        a2.set_ylim(ymin=0)
        f.canvas.draw()


        main.frames[GraphPage].values[len(data)+i].set("Battery Level: "+str(45)+"%")

        i+=1


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
        label = tk.Label(self, text="Water Level\nMonitoring System", font=("Helvetica", 64))
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Graphs", font=("Helvetica", 32),
                            command=lambda: controller.show_frame(GraphPage))
        button.pack()
        button2 = tk.Button(self, text="Settings", font=("Helvetica", 32),
                            command=lambda: controller.show_frame(SettingsPage))
        button2.pack()
        button3 = tk.Button(self, text="Information", font=("Helvetica", 32),
                            command=lambda: controller.show_frame(InfoPage))
        button3.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Information", font=("Helvetica", 32))
        label.pack()

        tk.Label(self, text="Creators", font=("Helvetica", 24)).pack()
        tk.Label(self, text="Connor O'Leary\nDavid Hamilton\nYue Gong", font=("Helvetica", 12)).pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


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
        # file = open('values.txt', 'r')
        # self.data = file.readlines()
        self.values = []
        for dat in data:
            val =  tk.StringVar()
            val.set(dat.replace('\n',''))
            self.values.append(val)
        print ("Tank 1: "+self.values[0].get())
        for f in figs:
            content = tk.StringVar()
            tk.Button(self, text=self.values[i*3].get(), textvariable=self.values[i*3], height = 1, width = 10, borderwidth=1, font=("Helvetica", 20),
                            command=lambda i=i: self.tank_rename(i)).grid(row=i*5+1,column=0,columnspan=2, padx=10)
            
            val =  tk.StringVar()
            lab = tk.Label(self, textvariable= val,font=("Helvetica", 16))
            self.values.append(val)
            lab.grid(row=i*5+2,column=0,columnspan=2,padx=10)

            tk.Label(self, text="Conversion Factors", font=("Helvetica", 12)).grid(row=i*5+3,column=0,columnspan=2,padx=10)
            tk.Label(self, text="Water:", font=("Helvetica", 12)).grid(row=i*5+4,column=0,padx=1)
            tk.Button(self, textvariable=self.values[i*3+1], 
                            height = 1, width = 4, borderwidth=1, font=("Helvetica", 12),
                            command=lambda i=i: self.conv_water(i)).grid(row=i*5+4,column=1,padx=10)
            tk.Label(self, text="Battery:", font=("Helvetica", 12)).grid(row=i*5+5,column=0,padx=1)
            tk.Button(self, textvariable=self.values[i*3+2], 
                            height = 1, width = 4, borderwidth=1, font=("Helvetica", 12),
                            command=lambda i=i: self.conv_battery(i)).grid(row=i*5+5,column=1,padx=10)
            

            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            #canvas.get_tk_widget().grid(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.grid(row=i*5+1,column=2, rowspan=5)

            i+=1

        button1 = tk.Button(self, text="Back to Home", height = 2, width = 14,
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(columnspan=3)

    def tank_rename(self, num):
        t = tk.Toplevel()
        tk.Label(t, text="Enter Tank "+str(num+1)+"'s name").pack(side="top", fill="both", expand=True, padx=10, pady=5)
        e = tk.Entry(t)
        e.pack(padx=10)
        button = tk.Button(t, text="Enter",
                            command=lambda: self.get_values(t, e.get(), 0, num)).pack()

    def conv_water(self, num):
        t = tk.Toplevel()
        tk.Label(t, text="Enter Tank "+str(num+1)+"'s water conversion").pack(side="top", fill="both", expand=True, padx=10, pady=5)
        e = tk.Entry(t)
        e.pack(padx=10)
        button = tk.Button(t, text="Enter",
                            command=lambda: self.get_values(t, e.get(), 1, num)).pack()

    def conv_battery(self, num):
        t = tk.Toplevel()
        tk.Label(t, text="Enter Tank "+str(num+1)+"'s battery conversion").pack(side="top", fill="both", expand=True, padx=10, pady=5)
        e = tk.Entry(t)
        e.pack(padx=10)
        button = tk.Button(t, text="Enter",
                            command=lambda: self.get_values(t, e.get(), 2, num)).pack()

    def get_values(self, t, string, context, num):
        data[3*num+context]=string+"\n"
        self.values[3*num+context].set(string)

        # with open('values.txt', 'r') as file:
        #     # read a list of lines into data
        #     data = file.readlines()

        # change the line 

        # and write everything back
        # print ("changing: " +string)
        with open('values.txt', 'w') as file:
            file.writelines(data)
        
        t.destroy()

main = mainP()
main.after(1, update, figs)
main.mainloop()
