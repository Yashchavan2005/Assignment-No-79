import tkinter as tk

root = tk.Tk()
root.title("Find The Larget Number")
root.geometry("400x300")


# Entry  Fisrt Number 
Label1 = tk.Label(root,text="Enter A Fisrt Number:")
Label1.pack()

Entry1 = tk.Entry(root)
Entry1.pack()

# Entry Second Number 
Label2 =  tk.Label(root,text="Enter A Second Number")
Label2.pack()

Entry2 = tk.Entry(root)
Entry2.pack()

# Entry Three Number

Label3 = tk.Label(root,text="Enter A Three Number")
Label3.pack()

Entry3 = tk.Entry(root)
Entry3.pack()

ResultLabel = tk.Label(root,text="")
ResultLabel.pack()

Button1 = tk.Button(
    root,
    text="Find Maximum",
    command =lambda:ResultLabel.config(
        text=f"Largest Number: {max(float(Entry1.get()), float(Entry2.get()),float(Entry3.get()))}"
    )
)

Button1.pack()

root.mainloop()


