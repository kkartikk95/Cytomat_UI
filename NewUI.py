from tkinter import *

commandList = {
    "load": "mv:ts ",
    "Unload": "mv:st ",
    "setpara": "se:pb ",
    "Start" : "ll:va",
    "Stop" : "ll:vd",
    "status": "ch:be",
    "Agitation Status": "ch:as"

}

def load():
    global commandList
    ldcmd = commandList["load"]
    val = ld.get()
    print(ldcmd+val+"\r")


def Unload():
    pass

def setparStrt():
    pass

def Stop():
    pass

def CheckStatus():
    pass


if __name__ == "__main__":
    root = Tk()
    root.title("Cytomat Control")
    root.geometry("1000x1000")

######### Load ################
    ld = Entry(root,width=20)
    ld.pack(pady=3)
    ldbtn = Button(root,text="Load",command=load)
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
    inventory = Button(root, text="Inventory", command=CheckStatus)
    inventory.pack(pady=3)


    root.mainloop()
