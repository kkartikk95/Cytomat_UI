from tkinter import *
from csv import *
from tkinter import *
from tkinter import messagebox

commandList = {
    "load": "mv:ts ",
    "Unload": "mv:st ",
    "setpara": "se:pb ",
    "Start" : "ll:va",
    "Stop" : "ll:vd",
    "status": "ch:be",
    "Agitation Status": "ch:as"

}

def statbox(v):
    boxentry.set(v)

#Load plate into Cytomat
def load():
    global commandList
    ldcmd = commandList["load"]
    val = ld.get()
    if val == "" or 0 <= int(val) > 150:
        v = "Please Enter value in range from 1-150"
        statbox(v)
        print("Entered")
    else:
        v = "Great! Working on it!"
        statbox(v)
    print(ldcmd+val+"\r")

#Unload plate from Cytomat
def Unload():
    global commandList
    ldcmd = commandList["load"]
    val = ld.get()
    if val == "" or 0 <= int(val) > 150:
        v = "Please Enter value in range from 1-150"
        statbox(v)
        print("Entered")
    else:
        v = "Great! Working on it!"
        statbox(v)
    print(ldcmd + val + "\r")

def setparStrt():
    val = param.get()
    cmd = "se:pb " + val + "\r"
    ser.write(cmd.encode())
    strt = status()
    if strt == "ok":
        cmd = "ll:va" + "\r"
        ser.write(cmd.encode())
    else:
        Label(root, text="Please recheck parameters", font=('Arial', 12), bg="red").grid(row=100, column=295)

def Stop():
    pass

def CheckStatus():
    pass

def inventory():
    window = Tk()
    window.title("Data Entry")
    window.geometry("700x350")
    main_lst = []

    def Add():
        global lst
        lst = [Plate_Name.get(), Location.get(), researcher.get(), date.get()]
        main_lst.append(lst)
        messagebox.showinfo("Information", "The data has been added successfully")

    def Save():
        with open("Cytomat_inventory.csv", "w") as file:
            Writer = writer(file)
            Writer.writerow(["Plate Name", "Location", "Researcher", "Date"])
            Writer.writerows(main_lst)
            messagebox.showinfo("Information", "Saved succesfully")

    def Delete():
        Plate_Name.delete(0, END)
        Location.delete(0, END)
        researcher.delete(0, END)
        date.delete(0, END)

    # 4 labels, 4 buttons,4 entry fields
    label1 = Label(window, text="Plate Name: ", padx=20, pady=10)
    label2 = Label(window, text="Location: ", padx=20, pady=10)
    label3 = Label(window, text="Researcher: ", padx=20, pady=10)
    label4 = Label(window, text="Date: ", padx=20, pady=10)

    Plate_Name = Entry(window, width=30, borderwidth=3)
    Location = Entry(window, width=30, borderwidth=3)
    researcher = Entry(window, width=30, borderwidth=3)
    date = Entry(window, width=30, borderwidth=3)

    save = Button(window, text="Save", padx=20, pady=10, command=Save)
    add = Button(window, text="Add", padx=20, pady=10, command=Add)
    delete = Button(window, text="Clear", padx=18, pady=10, command=Delete)
    Exit = Button(window, text="Exit", padx=20, pady=10, command=window.quit)

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=2, column=0)
    label4.grid(row=3, column=0)

    Plate_Name.grid(row=0, column=1)
    Location.grid(row=1, column=1)
    researcher.grid(row=2, column=1)
    date.grid(row=3, column=1)
    save.grid(row=7, column=0, columnspan=2)
    add.grid(row=6, column=0, columnspan=2)
    delete.grid(row=8, column=0, columnspan=2)
    Exit.grid(row=9, column=0, columnspan=2)

    window.mainloop()
    #print(lst)
    print(main_lst)


if __name__ == "__main__":
    root = Tk()
    root.title("Cytomat Control")
    root.geometry("1000x1000")
    boxentry = StringVar()

######### Load ################
    ld = Entry(root,width=20)
    ld.pack(pady=3)
    ldbtn = Button(root,text="Load", command=load)
    ldbtn.pack(pady=3)

######### Unload ################
    uld = Entry(root, width=20)
    uld.pack(pady=3)
    uldbtn = Button(root, text="Unload", command=Unload)
    uldbtn.pack(pady=3)

######### Set Parameters and Start ################
    setparstrt = Entry(root, width=20)
    setparstrt.pack(pady=3)
    setparstrtbtn = Button(root, text="Set parameters and Start", command=setparStrt)
    setparstrtbtn.pack(pady=3)

######### Stop ################
    stpbtn = Button(root, text="Stop", command=Stop)
    stpbtn.pack(pady=3)

######### Check Status ################
    chksts = Button(root, text="Check Status", command=CheckStatus)
    chksts.pack(pady=3)

###### Inventory ################
    inventory = Button(root, text="Inventory", command=inventory)
    inventory.pack(pady=3)

###### Status Box ################
    box = Entry(root,textvariable=boxentry, width=40)
    box.pack(pady=5)

    root.mainloop()
