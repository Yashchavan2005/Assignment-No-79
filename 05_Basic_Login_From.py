import tkinter as tk

Root = tk.Tk()
Root.title("Basic Logic From")
Root.geometry("400x250")

Label1 = tk.Label(Root,text="Enter UserName")
Label1.pack()

Entry1 = tk.Entry(Root)
Entry1.pack()

Label2 = tk.Label(Root , text= "Enter Password")
Label2.pack()

Entry2 = tk.Entry(Root,show="*")
Entry2.pack()

ResultLabel = tk.Label(Root,text="")
ResultLabel.pack()

Buuton1 = tk.Button(
    Root,
    text="Login",
    command=lambda :ResultLabel.config(
        text="Login Suceessfully"
        if Entry1.get() == "admin" and Entry2.get() == "1234"
        else "Inavlid UserName Password"
    )
)
Buuton1.pack()

Root.mainloop()