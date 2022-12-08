
import serial as serial
from csv import *
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl import load_workbook

#ser = serial.Serial("COM4", 9600, timeout=5)
b = 1

#---------------UNLOAD--------------#


def Unload():
    val = transferstation.get()
    if val == "" or 0 <= int(val) > 150:
        Label(root, text="Please input Unload location in range from (001-150)", font=('Arial', 12), bg="red").pack()
    else:
        
        cmd = "mv:st " + val + "\r"
        ser.write(cmd.encode())
        unldsts = status()
       
#---------------LOAD--------------#


def load():
    val = position.get()
    if val == "" or 0 <= int(val) > 150:
        Label(root, text="Please input load location in range from (001-150)", font=('Arial', 12), bg="red").pack()
    else:
        cmd = "mv:ts " + val + "\r"
        ser.write(cmd.encode())
        ldsts = status()

#---------------Set Parameters and Start--------------#


def start():
    val = param.get()
    print(val)
    cmd = "se:pb " + val + "\r"
    print(cmd)
    ser.write(cmd.encode())
    print(ser.write(cmd.encode()))
    strt = status()
    print(strt)
    f=Label(root, text="", font=('Arial', 12), bg="red")
    f.grid(row=11, column=100)
    if strt == "ok":
        cmd = "ll:va" + "\r"
        ser.write(cmd.encode())
        f.config(text = "Parameters Good", bg="green")
    else:
        f.config(text="Please recheck Parameters", bg="green")

#---------------Reset Error Bit--------------#


def reset():
    cmd = "rs:be" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    print(ret)

#---------------Check Status of Incubator and Agitation--------------#


def StatusCheck():
    # Error Bit check
    cmd = "ch:be" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    test = ret.decode()
    test = (test[3] + test[4])
    print("Test = ", test)
    sts = StringVar()
    sts.set("Will see the status here")
    f= Label(root, text="Will see the status here", font=('Arial', 12), bg="green")
    f.grid(row=102, column=100, pady=3)
    if test == "00":
        f.config(text="No errors")
    else:
        Button(root, text="Reset error (please press this button)", command=reset).grid(row=102, column=100, pady=3)

    # Agitation Status Check
    cmd = "ch:as" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    print(chr(ret[3]))
    stat = chr(ret[3])
    f = Label(root, text="Will see Agitation status here", font=('Arial', 12), bg="green")
    f.grid(row=100, column=100, pady=3)
    if stat == '0':
        f.config(text="Agitation is OFF")
    else:
        f.config(text="Agitation is ON")

    print("DONE")


def status():
    status = ser.read(10)
    status = status.decode()
    print(status[0])
    print(status[0] + status[1])
    result = status[0] + status[1]
    print(status)
    q = StringVar()
    q.set(result)
    f = Label(root, text="", font=('Arial', 12), bg="green")
    f.grid(row=101, column=100, pady=3)
    f.config(textvariable=q)
    return result

#---------------Stop Agitation--------------#


def stop():
    cmd = "ll:vd" + "\r"
    ser.write(cmd.encode())
    Label(root, text="Stopped", font=('Arial', 12), bg="Red").grid(row=103, column=100, pady=3)

#---------------Open Inventory for Add or Delete data--------------#


def inventory(b):
    window = Toplevel(root)
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
    #add = Button(window, text="Add", padx=20, pady=10, command=Add)
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
    #add.grid(row=6, column=0, columnspan=2)
    delete.grid(row=8, column=0, columnspan=2)
    Exit.grid(row=9, column=0, columnspan=2)

    #window.mainloop()
    # print(lst)
    print(main_lst)

#---------------Check Error--------------#
def error():
    cmd = "ch:be" + "\r"
    ser.write(cmd.encode())
    status = ser.read(10)
    print(status[2] + status[3])
    result = status[2] + status[3]
    print(result)


if __name__ == "__main__":
    root = Tk()
    root.title("Cytomat Control")
    root.geometry("900x900")
    # ______________LOAD_________________________________#
    position = Entry(root, width=20)
    position.grid(row=1, column=1, pady=4)

    label_pos = Label(root, text=" From TransferStation to Rack ")
    label_pos.grid(row=2, column=1, pady=4)

    pos_button = Button(root, text="Load (001-150)", command=load)
    pos_button.grid(row=3, column=1
                    , pady=4)
    # ______________UNLOAD_________________________________#
    transferstation = Entry(root, width=20)
    transferstation.grid(row=5, column=1, pady=4)

    label_transfer = Label(root, text=" From Racks to TransferStation ")
    label_transfer.grid(row=6, column=1, pady=4)

    pos_button = Button(root, text="Unload (001-150)", command=Unload)
    pos_button.grid(row=7, column=1, pady=4)
    # ______________SET PARAMETERS_________________________________#
    param = Entry(root, width=20)
    param.grid(row=9, column=1, pady=4)

    label_param = Label(root, text=" Set parameters for RPM and Distance\n"
                                   "Eg: 090(rpm) 018(distance) \n"
                                   "Always 3 digits for RPM and Distance each")
    label_param.grid(row=10, column=1, pady=4)

    Setpara_button = Button(root, text="Set Parameters and Start", command=start)
    Setpara_button.grid(row=11, column=1, pady=4)
    # ______________Check Status_________________________________#
    chk_sts = Button(root, text="Check Status", command=StatusCheck)
    chk_sts.grid(row=15, column=1, pady=4)

    # ______________STOP_________________________________#
    Stop_button = Button(root, text="Stop", command=stop)
    Stop_button.grid(row=18, column=1, pady=4)

    record = Button(root, text="Inventory", command=lambda: inventory(b))
    record.grid(row=19, column=1, pady=4)

    root.mainloop()
