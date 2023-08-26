from tkinter import*
from tkinter import ttk



class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Integrated Library Management System")
        self.root.geometry("1550x800+0+0")


        lbltitle = Label(self.root, text = "INTEGRATED LIBRARY MANAGEMENT SYSTEM", bg = "black", fg = "white", bd = 12, relief = RIDGE, font=("times new roman", 40, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg="#EEDFCC")
        frame.place(x = 0, y = 110, width=1530, height=430)


        #DATAFRAMELEFT
        DataFrameLeft=LabelFrame(frame, text = "Membership", bg = "#EEDFCC", fg = "#006400", bd = 10, relief = RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 380 )

        lblMemebr = Label(DataFrameLeft, bg="#EEDFCC", text = "Member Type", font=("arial", 12, "bold"),padx= 2, pady = 6)
        lblMemebr.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12, "bold"), width = 27, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)


        DataFrameRight=LabelFrame(frame, text = "Book Details", bg = "#EEDFCC", fg = "#006400", bd = 10, relief = RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 560, height = 380 )

        #BUTTONS FRAME
        Framebutton = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        Framebutton.place(x = 0, y = 540, width=1530, height=70)

        #INFORMATION FRAME
        FrameDetails = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        FrameDetails.place(x = 0, y = 610, width=1530, height=195)



        





if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()   
        