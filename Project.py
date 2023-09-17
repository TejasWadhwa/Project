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

        lblPRN_NO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, bg = "#EEDFCC")
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg = "#EEDFCC")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FirstName:", padx=2, pady=4, bg = "#EEDFCC")
        lblFirstName.grid(row=3, column=0, sticky=W)
        lblFirstName=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LastName:", padx=2, pady=4, bg = "#EEDFCC")
        lblLastName.grid(row=4, column=0, sticky=W)
        lblLastName=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 1:", padx=2, pady=4, bg = "#EEDFCC")
        lblAddress1.grid(row=5, column=0, sticky=W)
        lblAddress1=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 2:", padx=2, pady=4, bg = "#EEDFCC")
        lblAddress2.grid(row=6, column=0, sticky=W)
        lblAddress2=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=4, bg = "#EEDFCC")
        lblPostCode.grid(row=7, column=0, sticky=W)
        lblPostCode=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=4, bg = "#EEDFCC")
        lblMobile.grid(row=8, column=0, sticky=W)
        lblMobile=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, pady=4, bg = "#EEDFCC")
        lblBookId.grid(row=0, column=2, sticky=W)
        lblBookId=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=4, bg = "#EEDFCC")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        lblBookTitle=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=4, bg = "#EEDFCC")
        lblAuther.grid(row=2, column=2, sticky=W)
        lblAuther=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblAuther.grid(row=2, column=3)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=4, bg = "#EEDFCC")
        lblAuther.grid(row=2, column=2, sticky=W)
        lblAuther=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateDue.grid(row=4, column=2, sticky=W)
        lblDateDue=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=4, bg = "#EEDFCC")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Rerturn Fine:", padx=2, pady=4, bg = "#EEDFCC")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblLateReturnFine.grid(row=6, column=3)

        lblDateOverDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        lblDateOverDate=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblDateOverDate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=4, bg = "#EEDFCC")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        lblActualPrice=Entry(DataFrameLeft, font=("arial", 13, "bold"),width=29)
        lblActualPrice.grid(row=8, column=3)


        #DATAFRAMERIGHT
        DataFrameRight=LabelFrame(frame, text = "Book Details", bg = "#EEDFCC", fg = "#006400", bd = 10, relief = RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 560, height = 380 )

        self.txtBox=Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBoooks = ['Head Firt Book', 'Learn Python the Hard Way', 'Python Programming', 'Secrete Rahshy', 'Python Cookbook', 'Into to Machine Learning', 'Fluent Python', 'programming Python', 'The Algorithm', 'The technique Pyhton', 'Machine tecno', 'My Pyhton', 'Joss Ellif guru', 'Elite Jungle Python', 'Jungli Python', 'Mumbai Python', 'Pune Python', 'Guru of Python', 'Yellow Dragan', 'Red Python', 'Machine Python', 'Advance Python', 'Inton Python', 'RedChilli Python', 'Ishq Python']

        listBox=Listbox(DataFrameRight, font=("arial", 11, "bold"), width=20, height=16)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)

        #BUTTONS FRAME
        Framebutton = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        Framebutton.place(x = 0, y = 540, width=1530, height=70)

        btnAddData=Button(Framebutton,text="Add Data",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,text="Show Data",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Exit",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,text="Add Data",  font=("arial", 12,"bold"), width=23,bg="azure",fg="black")
        btnAddData.grid(row=0,column=5)

        #INFORMATION FRAME
        FrameDetails = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        FrameDetails.place(x = 0, y = 610, width=1530, height=195)


if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()   

