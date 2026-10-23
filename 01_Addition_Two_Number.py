import tkinter as tk

root = tk.Tk()
root.title("Addition Of Two Numbers")
root.geometry("300x200")

tk.Label(root,text="Enter A Fisrt Number:").pack()
Entry1 = tk.Entry(root)
Entry1.pack()

tk.Label(root,text="Enter A Second Number:").pack()
Entry2 = tk.Entry(root)
Entry2.pack()

Resultlabel = tk.Label(root,text="")
Resultlabel.pack()

tk.Button(
    root,
    text="Add",
    command=lambda:Resultlabel.config(
        text=f"Addition= {float(Entry1.get())+ float(Entry2.get())}"
    )
).pack()

root.mainloop()