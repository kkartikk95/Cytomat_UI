from tkinter import *
from tkinter import ttk

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
    pass

def Stop():
    pass

def CheckStatus():
    pass

def inventory():
    table_frame = Frame(root)
    table_frame.pack()

    myinventory = ttk.Treeview(table_frame)
    myinventory['columns'] = ('Rack 1', 'Rack 2', 'Rack 3', 'Rack 4', 'Rack 5',
                              'Rack 6', 'Rack 7', 'Rack 8', 'Rack 9', 'Rack 10')
    myinventory.column("Rack 1", anchor=CENTER, width=50)
    myinventory.column("Rack 2", anchor=CENTER, width=50)
    myinventory.column("Rack 3", anchor=CENTER, width=50)
    myinventory.column("Rack 4", anchor=CENTER, width=50)
    myinventory.column("Rack 5", anchor=CENTER, width=50)
    myinventory.column("Rack 6", anchor=CENTER, width=50)
    myinventory.column("Rack 7", anchor=CENTER, width=50)
    myinventory.column("Rack 8", anchor=CENTER, width=50)
    myinventory.column("Rack 9", anchor=CENTER, width=50)
    myinventory.column("Rack 10", anchor=CENTER, width=50)

    myinventory.heading("Rack 1", text="Rack 1", anchor=CENTER)
    myinventory.heading("Rack 2", text="Rack 2", anchor=CENTER)
    myinventory.heading("Rack 3", text="Rack 3", anchor=CENTER)
    myinventory.heading("Rack 4", text="Rack 4", anchor=CENTER)
    myinventory.heading("Rack 5", text="Rack 5", anchor=CENTER)
    myinventory.heading("Rack 6", text="Rack 6", anchor=CENTER)
    myinventory.heading("Rack 7", text="Rack 7", anchor=CENTER)
    myinventory.heading("Rack 8", text="Rack 8", anchor=CENTER)
    myinventory.heading("Rack 9", text="Rack 9", anchor=CENTER)
    myinventory.heading("Rack 10", text="Rack 10", anchor=CENTER)

    myinventory.insert(parent='',index='end', values=('10', 'B00-HPC', '101', 'Oklahoma', 'Moore'))

    myinventory.pack(pady=5)
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
