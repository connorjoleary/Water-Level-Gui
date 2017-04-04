import tkinter as tk

def tank_rename(num):
    t = tk.Toplevel()
    tk.Label(t, text="Enter Tank "+str(num)+"'s name").pack(side="top", fill="both", expand=True, padx=10, pady=5)
    e = tk.Entry(t)
    e.pack(padx=10)
    button = tk.Button(t, text="Enter",
                        command=lambda: get_values(t, e.get(), 1, num)).pack()

def conv_factors(num):
    t = tk.Toplevel()
    l = tk.Label(t, text="Here")
    l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

def get_values(t, string, context, num):
    with open('values.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    # change the line
    data[num*context] = string

    # and write everything back
    with open('stats.txt', 'w') as file:
        file.writelines( data )
    t.destroy()