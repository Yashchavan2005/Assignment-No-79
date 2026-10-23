import tkinter  as tk

Root = tk.Tk()
Root.title("Voting Eligblity Checker")
Root.geometry("400x250")


# ENter Name  # Label 1
Label1 = tk.Label(Root,text="Enter Name")
Label1.pack()

Entry1 = tk.Entry(Root)
Entry1.pack()

# Entry Name # Label 2

Lable2 = tk.Label(Root,text ="Enter Age")
Lable2.pack()

Entry2 = tk.Entry(Root)
Entry2.pack()

ResultLabel = tk.Label(Root , text="")
ResultLabel.pack()

Buuton1 = tk.Button(
    Root,
    text="Check Eligiblity",
    command=lambda:ResultLabel.config(
        text=f"{Entry1.get()} is {"Eligible" if int(Entry2.get()) >= 18 else "Not Eligble"}to vote"

    )
    
)
Buuton1.pack()

Root.mainloop()



