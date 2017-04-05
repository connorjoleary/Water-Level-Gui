import tkinter as tk

# def tank_rename(num):
#     t = tk.Toplevel()
#     tk.Label(t, text="Enter Tank "+str(num)+"'s name").pack(side="top", fill="both", expand=True, padx=10, pady=5)
#     e = tk.Entry(t)
#     e.pack(padx=10)
#     button = tk.Button(t, text="Enter",
#                         command=lambda: get_values(t, e.get(), 1, num)).pack()

# def conv_factors(self, num):
#     t = tk.Toplevel()
#     tk.Label(t, text="Enter Tank "+str(num+1)+"'s Water Conversion Factor").pack(side="top", fill="both", expand=True, padx=10, pady=5)
#     e = tk.Entry(t)
#     e.pack(padx=10)
#     button = tk.Button(t, text="Enter",
#                         command=lambda: self.get_values(t, e.get(), 1, num)).pack()
#     tk.Label(t, text="Enter Tank "+str(num+1)+"'s Battery Conversion Factor").pack(side="top", fill="both", expand=True, padx=10, pady=5)
#     e2 = tk.Entry(t)
#     e2.pack(padx=10)
#     button = tk.Button(t, text="Enter",
#                         command=lambda: self.get_values(t, e2.get(), 2, num)).pack()

# # def get_values(t, string, context, num):
#     with open('values.txt', 'r') as file:
#         # read a list of lines into data
#         data = file.readlines()

#     # change the line
#     data[num*context] = string+"\n"

#     # and write everything back
#     with open('values.txt', 'w') as file:
#         file.writelines(data)
    
#     t.destroy()