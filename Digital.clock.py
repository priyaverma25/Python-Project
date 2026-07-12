# import tkinter as tk
# from time import strftime

# root = tk.Tk()
# root.title("Digital Clock")

# def time():
#     string = str('%H:%M:%S %p\n%d/%m/%Y')
#     label.config(text=string)
#     label.after(1000,time)
 
# label = tk.Label(
#     root, 
#     font=('calibri', 50, 'bold'),
#     background='yellow',
#     foreground='black')    

# label.pack(anchor='center')

# time()

# root.mainloop()


import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S %p\n%d/%m/%Y")
    label.config(text=current_time)
    label.after(1000, update_time)

label = tk.Label(root, font=("Calibri", 40, "bold"),
                 bg="yellow", fg="black")
label.pack()

update_time()
root.mainloop()






