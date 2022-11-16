from csv import *
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Data Entry")
window.geometry("700x350")
main_lst=[]

def Add():
  global lst
  lst = [Plate_Name.get(),Location.get(),researcher.get(), date.get()]
  main_lst.append(lst)
  messagebox.showinfo("Information","The data has been added successfully")

def Save():
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Plate Name","Location","Researcher", "Date"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

def Clear():
   Plate_Name.delete(0,END)
   Location.delete(0,END)
   researcher.delete(0,END)
   date.delete(0,END)

# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Plate Name: ",padx=20,pady=10)
label2=Label(window,text="Location: ",padx=20,pady=10)
label3=Label(window,text="Researcher: ",padx=20,pady=10)
label4=Label(window,text="Date: ",padx=20,pady=10)

Plate_Name=Entry(window,width=30,borderwidth=3)
Location=Entry(window,width=30,borderwidth=3)
researcher=Entry(window,width=30,borderwidth=3)
date = Entry(window,width=30,borderwidth=3)

save=Button(window,text="Save",padx=20,pady=10,command=Save)
add=Button(window,text="Add",padx=20,pady=10,command=Add)
clear=Button(window,text="Clear",padx=18,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)

Plate_Name.grid(row=0,column=1)
Location.grid(row=1,column=1)
researcher.grid(row=2,column=1)
date.grid(row=3,column=1)
save.grid(row=7,column=0,columnspan=2)
add.grid(row=6,column=0,columnspan=2)
clear.grid(row=8,column=0,columnspan=2)
Exit.grid(row=9,column=0,columnspan=2)

window.mainloop()
print(lst)
print(main_lst)