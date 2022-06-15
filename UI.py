from tkinter import *
import serial as serial

#ser = serial.Serial("COM3", 9600, timeout=5)
b = 1


def Destroy(e):
    e.after(10000, e.destroy())


def Unload():
    val = transferstation.get()
    if val == "" or 0 <= int(val) > 150:
        Label(root, text="Please input Unload location in range from (001-150)", font=('Arial', 12), bg="red").pack()
    else:
        cmd = "mv:st " + val + "\r"
        ser.write(cmd.encode())
        unldsts = status()


def load():
    val = position.get()
    if val == "" or 0 <= int(val) > 150:
        Label(root, text="Please input load location in range from (001-150)", font=('Arial', 12), bg="red").pack()
    else:
        cmd = "mv:ts " + val + "\r"
        ser.write(cmd.encode())
        ldsts = status()


def start():
    val = param.get()
    cmd = "se:pb " + val + "\r"
    ser.write(cmd.encode())
    strt = status()
    if strt == "ok":
        cmd = "ll:va" + "\r"
        ser.write(cmd.encode())
    else:
        Label(root, text="Please recheck parameters", font=('Arial', 12), bg="red").grid(row=100, column=295)


def reset():
    cmd = "rs:be" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    print(ret)


def StatusCheck():
    # Error Bit check
    cmd = "ch:be" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    test = ret.decode()
    test = test[3] + test[4]
    q = StringVar()
    q.set(ret)
    Label(root, textvariable=q, font=('Arial', 12), bg="green").grid(row=101, column=100, pady=3)
    if test == "00":
        e = Label(root, text="No errors", font=('Arial', 12), bg="green")
        e.grid(row=102, column=100, pady=3)

    else:
        Button(root, text="Reset error (please press this button)", command=reset).grid(row=102, column=100, pady=3)

    # Agitation Status Check
    cmd = "ch:as" + "\r"
    ser.write(cmd.encode())
    ret = ser.read(10)
    print(chr(ret[3]))
    stat = chr(ret[3])
    if stat == '0':
        Label(root, text="Agitation is OFF", font=('Arial', 12), bg="green").grid(row=100, column=100, pady=3)
    else:
        Label(root, text="Agitation is ON", font=('Arial', 12), bg="green").grid(row=100, column=100, pady=3)

    Destroy(e)


def status():
    status = ser.read(10)
    status = status.decode()
    print(chr(status[0]) + chr(status[1]))
    result = chr(status[0]) + chr(status[1])
    print(status)
    q = StringVar()
    q.set(status)
    Label(root, textvariable=q, font=('Arial', 12), bg="green").grid(row=101, column=100, pady=3)
    return result


def stop():
    cmd = "ll:vd" + "\r"
    ser.write(cmd.encode())
    Label(root, text="Stopped", font=('Arial', 12), bg="Red").grid(row=103, column=100, pady=3)


def inventory(b):
    # Toplevel object which will
    # be treated as a new window
    table = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    table.title("Inventory")

    # sets the geometry of toplevel
    table.geometry("1000x1000")
    for i in range(1, 16):
        for j in range(2, 21, 2):
            e = Entry(table, width=15, bg="lightblue", fg="black")
            e.grid(row=i, column=j)
    for i in range(1, 16):
        for j in range(1, 21, 2):
            a = StringVar()
            a.set(b)
            f = Label(table
                      , textvariable=a)
            f.grid(row=i, column=j)
            b = b + 1


def error():
    cmd = "ch:be" + "\r"
    ser.write(cmd.encode())
    status = ser.read(10)
    print(chr(status[2]) + chr(status[3]))
    result = chr(status[2]) + chr(status[3])
    print(result)


if __name__ == "__main__":
    root = Tk()
    root.title("Cytomat Control")
    root.geometry("2736x1824")
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
