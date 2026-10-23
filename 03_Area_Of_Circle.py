import tkinter as tk

Root = tk.Tk()
Root.title("Area Of Circle")
Root.geometry("400x250")

Label1 = tk.Label(Root,text="Entry Radius")
Label1.pack()

Entry1 = tk.Entry(Root)
Entry1.pack()

ResultLabel = tk.Label(Root,text="")
ResultLabel.pack()

Buuton1 = tk.Button(
    Root,
    text="Calculate Area",
    command=lambda:ResultLabel.config(
        text=f"Area of circle:{3.14 *float(Entry1.get()) **2}"
    )
)

Buuton1.pack()

Root.mainloop()
