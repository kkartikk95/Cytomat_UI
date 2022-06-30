from tkinter import *
import sqlite3

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
    pass

def Stop():
    pass

def CheckStatus():
    pass

def del_database():
    con = sqlite3.connect('inventory.db')
    c = con.cursor()

    c.execute("DROP table inventory")

def database():
    con = sqlite3.connect('inventory.db')
    c = con.cursor()
    c.execute(""" CREATE TABLE inventory (
        Location int,
        Plate_Name text )  
    """)
def inventory():
    con = sqlite3.connect('inventory.db')
    c = con.cursor()
    c.execute("SELECT * FROM inventory")
    records = c.fetchall()
    display_record = ''
    for record in records:
        display_record += str(record) + "\n"

    query_label = Label(root,text=display_record)
    query_label.pack(pady=5)


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
    inventory = Button(root, text="Inventory", command=database)
    inventory.pack(pady=3)

###### Status Box ################
    box = Entry(root,textvariable=boxentry, width=40)
    box.pack(pady=5)


    root.mainloop()
