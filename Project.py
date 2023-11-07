from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Integrated Library Management System")
        self.root.geometry("1550x800+0+0")

        

        #VARIABLE
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()



        lbltitle = Label(self.root, text = "DIGITAL LIBRARY", bg = "black", fg = "white", bd = 12, relief = RIDGE, font=("times new roman", 40, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg="#EEDFCC")
        frame.place(x = 0, y = 110, width=1530, height=430)


        #DATAFRAMELEFT
        DataFrameLeft=LabelFrame(frame, text = "Membership", bg = "#EEDFCC", fg = "#006400", bd = 10, relief = RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 380 )

        lblMember = Label(DataFrameLeft, bg="#EEDFCC", text = "Member Type:", textvariable= self.member_var, font=("arial", 12, "bold"),padx= 2, pady = 6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12, "bold"), width = 27, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        
        lblPRN_NO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, bg = "#EEDFCC")
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg = "#EEDFCC")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FirstName:", padx=2, pady=4, bg = "#EEDFCC")
        lblFirstName.grid(row=3, column=0, sticky=W)
        lblFirstName=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        lblFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LastName:", padx=2, pady=4, bg = "#EEDFCC")
        lblLastName.grid(row=4, column=0, sticky=W)
        lblLastName=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        lblLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 1:", padx=2, pady=4, bg = "#EEDFCC")
        lblAddress1.grid(row=5, column=0, sticky=W)
        lblAddress1=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=29)
        lblAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 2:", padx=2, pady=4, bg = "#EEDFCC")
        lblAddress2.grid(row=6, column=0, sticky=W)
        lblAddress2=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=29)
        lblAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=4, bg = "#EEDFCC")
        lblPostCode.grid(row=7, column=0, sticky=W)
        lblPostCode=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width=29)
        lblPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=4, bg = "#EEDFCC")
        lblMobile.grid(row=8, column=0, sticky=W)
        lblMobile=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        lblMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, pady=4, bg = "#EEDFCC")
        lblBookId.grid(row=0, column=2, sticky=W)
        lblBookId=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width=29)
        lblBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=4, bg = "#EEDFCC")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        lblBookTitle=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var, width=32)
        lblBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=4, bg = "#EEDFCC")
        lblAuther.grid(row=2, column=2, sticky=W)
        lblAuther=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.auther_var, width=29)
        lblAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateborrowed_var, width=29)
        lblDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateDue.grid(row=4, column=2, sticky=W)
        lblDateDue=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.datedue_var, width=29)
        lblDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=4, bg = "#EEDFCC")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.daysonbook_var, width=29)
        lblDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Rerturn Fine:", padx=2, pady=4, bg = "#EEDFCC")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.latereturnfine_var, width=29)
        lblLateReturnFine.grid(row=6, column=3)

        lblDateOverDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=4, bg = "#EEDFCC")
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        lblDateOverDate=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=29)
        lblDateOverDate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=4, bg = "#EEDFCC")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        lblActualPrice=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.finalprice_var, width=29)
        lblActualPrice.grid(row=8, column=3)


        #DATAFRAMERIGHT
        DataFrameRight=LabelFrame(frame, text = "Book Details", bg = "#EEDFCC", fg = "#006400", bd = 10, relief = RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 560, height = 380 )

        self.txtBox=Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        

        listBoooks = ['Atomic Habits', 'Principles', 'The Psychology of Money', 'Mindset', 'Rich Dad Poor Dad', 'The Miracle Morning', 'Trillions', 'The School of Life', 'The Oracle of Night', 'Designing Your Life', 'Emotional Intelligence', 'My Age Of Anxiety', 'Words Can Change Your Brain', 'Stumbling On Happiness', 'The Paradox Of Choice', 'The Honest Truth About Dishonesty', 'The Upside Of Your Dark Side', 'Thinking Fast And Slow', 'The Dictionary of Body Language', 'Games People Play', "Don't Believe Everything You Think", 'The Automatic Millionaire', 'The One-Page Financial Plan', 'Secrets Of The Millionaire Mind', 'The Total Money Makeover']
        
        #FILLDATA
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x=="Atomic Habits"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Atomic Habits")
                self.auther_var.set("James Clear")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")

            elif (x=="Principles"):
                self.bookid_var.set("BKID4578")
                self.booktitle_var.set("Principles")
                self.auther_var.set("Ray Dalio")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.750")

            elif (x=="The Psychology of Money"):
                self.bookid_var.set("BKID2232")
                self.booktitle_var.set("The Psychology of Money")
                self.auther_var.set("Morgan Housel")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(11)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.760")

            elif (x=="Mindset"):
                self.bookid_var.set("BKID6680")
                self.booktitle_var.set("Mindset")
                self.auther_var.set("Carol Dweck")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.760")

            elif (x=="Rich Dad Poor Dad"):
                self.bookid_var.set("BKID7908")
                self.booktitle_var.set("Rich Dad Poor Dad")
                self.auther_var.set("Robert T. Kiyosaki")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(20)
                self.latereturnfine_var.set("Rs.100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif (x=="The Miracle Morning"):
                self.bookid_var.set("BKID2990")
                self.booktitle_var.set("The Miracle Morning")
                self.auther_var.set("Hal Elrod")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(30)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif (x=="Trillions"):
                self.bookid_var.set("BKID3888")
                self.booktitle_var.set("Trillions")
                self.auther_var.set("Robin Wigglesworth")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(22)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.880")

            elif (x=="The School of Life"):
                self.bookid_var.set("BKID4690")
                self.booktitle_var.set("The School of Life")
                self.auther_var.set("Alain de Botton")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(30)
                self.latereturnfine_var.set("Rs.70")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.880")

            elif (x=="The Oracle of Night"):
                self.bookid_var.set("BKID8888")
                self.booktitle_var.set("The Oracle of Night")
                self.auther_var.set("Sidarta Ribeiro")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(40)
                self.latereturnfine_var.set("Rs.150")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1200")

            elif (x=="Designing Your Life"):
                self.bookid_var.set("BKID0089")
                self.booktitle_var.set("Designing Your Life")
                self.auther_var.set("Bill Burnett")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(28)
                self.latereturnfine_var.set("Rs.90")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1150")

            elif (x=="Emotional Intelligence"):
                self.bookid_var.set("BKID1334")
                self.booktitle_var.set("Emotional Intelligence")
                self.auther_var.set("Daniel Goleman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(18)
                self.latereturnfine_var.set("Rs.90")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.900")

            elif (x=="My Age Of Anxiety"):
                self.bookid_var.set("BKID1666")
                self.booktitle_var.set("My Age Of Anxiety")
                self.auther_var.set("Scott Stossel")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(25)
                self.latereturnfine_var.set("Rs.110")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")

            elif (x=="Words Can Change Your Brain"):
                self.bookid_var.set("BKID4789")
                self.booktitle_var.set("Words Can Change Your Brain")
                self.auther_var.set("Andrew B. Newberg")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(11)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.690")

            elif (x=="Stumbling On Happiness"):
                self.bookid_var.set("BKID9999")
                self.booktitle_var.set("Stumbling On Happiness")
                self.auther_var.set("Dan Gilbert")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(23)
                self.latereturnfine_var.set("Rs.100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1200")

            elif (x=="The Paradox Of Choice"):
                self.bookid_var.set("BKID4678")
                self.booktitle_var.set("The Paradox Of Choice")
                self.auther_var.set("Barry Schwartz")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="The Honest Truth About Dishonesty"):
                self.bookid_var.set("BKID4490")
                self.booktitle_var.set("The Honest Truth About Dishonesty")
                self.auther_var.set("Dan Ariely")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(20)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.550")

            elif (x=="The Upside Of Your Dark Side"):
                self.bookid_var.set("BKID2009")
                self.booktitle_var.set("The Upside Of Your Dark Side")
                self.auther_var.set("Todd Kashdan")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(20)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.550")

            elif (x=="Thinking Fast And Slow"):
                self.bookid_var.set("BKID4545")
                self.booktitle_var.set("Thinking Fast And Slow")
                self.auther_var.set("Daniel Kahneman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(40)
                self.latereturnfine_var.set("Rs.60")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif (x=="The Dictionary of Body Language"):
                self.bookid_var.set("BKID0090")
                self.booktitle_var.set("The Dictionary of Body Language")
                self.auther_var.set("Joe Navarro")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.60")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.680")

            elif (x=="Games People Play"):
                self.bookid_var.set("BKID121")
                self.booktitle_var.set("Games People Play")
                self.auther_var.set("Eric Berne")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(30)
                self.latereturnfine_var.set("Rs.110")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.850")

            elif (x=="Don't Believe Everything You Think"):
                self.bookid_var.set("BKID4490")
                self.booktitle_var.set("Don't Believe Everything You Think")
                self.auther_var.set("Joseph Nguyen")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(32)
                self.latereturnfine_var.set("Rs.100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.800")

            elif (x=="The Automatic Millionaire"):
                self.bookid_var.set("BKID9997")
                self.booktitle_var.set("The Automatic Millionaire")
                self.auther_var.set("David Bach")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(40)
                self.latereturnfine_var.set("Rs.200")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1150")

            elif (x=="The One-Page Financial Plan"):
                self.bookid_var.set("BKID7777")
                self.booktitle_var.set("The One-Page Financial Plan")
                self.auther_var.set("Carl Richards")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(21)
                self.latereturnfine_var.set("Rs.220")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1200")

            elif (x=="Secrets Of The Millionaire Mind"):
                self.bookid_var.set("BKID0001")
                self.booktitle_var.set("Secrets Of The Millionaire Mind")
                self.auther_var.set("T. Harv Eker")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(50)
                self.latereturnfine_var.set("Rs.300")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1500")

            elif (x=="The Total Money Makeover"):
                self.bookid_var.set("BKID0359")
                self.booktitle_var.set("The Total Money Makeover")
                self.auther_var.set("Dave Ramsey")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(35)
                self.latereturnfine_var.set("Rs.150")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.950")

            
        listBox=Listbox(DataFrameRight, font=("arial", 11, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)

        #BUTTONS FRAME
        Framebutton = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        Framebutton.place(x = 0, y = 540, width=1530, height=70)

        btnAddData=Button(Framebutton, command=self.add_data, text="ADD DATA",  font=("arial", 12,"bold"), width=23 ,bg="white",fg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton, command=self.showData, text="SHOW DATA",  font=("arial", 12,"bold"), width=23,bg="#1E90FF",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="UPDATE",  font=("arial", 12,"bold"), width=23,bg="#00C957",fg="black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="DELETE",  font=("arial", 12,"bold"), width=23,bg="black",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton, command=self.reset, text="RESET",  font=("arial", 12,"bold"), width=23,bg="#00FFFF",fg="black")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="EXIT",  font=("arial", 12,"bold"), width=23,bg="#EE0000",fg="black")
        btnAddData.grid(row=0,column=5)

        #INFORMATION FRAME
        FrameDetails = Frame(self.root, bd = 10, relief=RIDGE, padx=20, bg="#EEDFCC")
        FrameDetails.place(x = 0, y = 610, width=1530, height=195)

        Table_frame=Frame(FrameDetails,bd = 6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("member","prnno","idno","firstname","lastname",
                                        "address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                        "datedue","days","laterreturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill="x")
        yscroll.pack(side=RIGHT, fill="y")

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("member",text="Member")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("idno", text="ID No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post Id")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date_due")
        self.library_table.heading("days", text="DaysOnBooks")
        self.library_table.heading("laterreturnfine", text="LaterReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("member", width=125)
        self.library_table.column("prnno", width=90)
        self.library_table.column("idno", width=90)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=120)
        self.library_table.column("address2", width=120)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("laterreturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Professor1348", database = "my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Sucess", "Member Inserted Successfully")
    
    def update(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Professor1348", database = "my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,BookTitle=%s,Auther=%s,Dateborrowed=%s,Datedue=%s,daysofbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
             self.member_var.get(),
             self.id_var.get(),
             self.firstname_var.get(),
             self.lastname_var.get(),
             self.address1_var.get(),
             self.address2_var.get(),
             self.postcode_var.get(),
             self.mobile_var.get(),
             self.bookid_var.get(),
             self.booktitle_var.get(),
             self.auther_var.get(),
             self.dateborrowed_var.get(),
             self.datedue_var.get(),
             self.daysonbook_var.get(),
             self.latereturnfine_var.get(),
             self.dateoverdue_var.get(),
             self.finalprice_var.get(),
             self.prn_var.get()
        ))
    
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member Updated !")


    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Professor1348", database = "my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row= self.library_table.focus()
        content= self.library_table.item(cursor_row)
        row= content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    #SHOW_DATA
    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN NO:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address 1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address 2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "LateReturnFine\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "FinalPrice\t\t"+ self.finalprice_var.get() + "\n")


    #RESET_DATA
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0", END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit ?")
        if iExit>0: 
            self.root.destroy()
            return
    
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
          messagebox.showerror("Error","First Select The Member")
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Professor1348", database = "my_data")
            my_cursor = conn.cursor()
            query="Delete from library where PRN_no=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member Deleted !")



if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()   

