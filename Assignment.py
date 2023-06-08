from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()
root = tk.Tk()
root.geometry("500x300")

def clicked():
    amount = int(entry_1.get())
    currency_1 = entry_2.get()
    currency_2 = entry_3.get()
    data = a.convert(amount,currency_1,currency_2)
    label_5 = tk.Label(root,text=data).place(x = 230,y = 250)

label_1 = tk.Label(root,text="CURRENCY CONVERTER",font = "calibri 20 bold").place(x = 120,y = 10)
label_2 = tk.Label(root,text="Enter amount: ",font = "calibri").place(x = 80,y = 60)
entry_1 = tk.Entry(root)

label_3 = tk.Label(root,text="Enter currency: ",font = "calibri").place(x = 80,y = 110)
entry_2 = tk.Entry(root)
label_4 = tk.Label(root,text="Enter required currency: ",font = "calibri").place(x = 80,y = 160)
entry_3 = tk.Entry(root)

button = tk.Button(root,text="click",command=clicked).place(x = 230,y = 210)
entry_1.place(x = 300,y = 65)
entry_2.place(x = 300,y = 115)
entry_3.place(x = 300,y = 165)

root.mainloop()
