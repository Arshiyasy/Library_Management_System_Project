from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
                def __init__(self, root):
                        self.root = root
                        self.root.title("Library Management System")
                        self.root.geometry("1550x800+0+0")

                        #==================================variable==============================================
                        self.MemberType_var=StringVar()
                        self.PRN_no_var=StringVar()
                        self.Title_var=StringVar()
                        self.FirstName_var=StringVar()
                        self.LastName_var=StringVar()
                        self.Address1_var=StringVar()
                        self.Address2_var=StringVar()
                        self.PostCode_var=StringVar()
                        self.Mobile_var=StringVar()
                        self.BookID_var=StringVar()
                        self.BookTitle_var=StringVar()
                        self.AuthorName_var=StringVar()
                        self.BorrowedDate_var=StringVar()
                        self.DueDate_var=StringVar()
                        self.NoOfDays_var=StringVar()
                        self.LateReturnFine_var=StringVar()
                        self.OverDue_var=StringVar()
                        self.ActualPrice_var=StringVar()



                        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="rosy brown",fg="IndianRed4",bd=20,relief=RIDGE,
                                font=("time new roman",50,"bold"),padx=2,pady=6)
                        lbltitle.pack(side=TOP,fill=X)


                        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="rosy brown")
                        frame.place(x=0,y=130,width=1535,height=400)


                #========================================================================================================
                #--------------------------DATAFRAME LEFT---------------------------------------------------------------#
                        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="rosy brown",fg="black",bd=12,relief=RIDGE,
                                                font=("time new roman",15,"bold"))
                        DataFrameLeft.place(x=0,y=5,width=900,height=350)

                        #Member Type
                        lblMember=Label(DataFrameLeft,bg="rosy brown",text="Member Type",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblMember.grid(row=0,column=0,sticky=W)
                        comMember=ttk.Combobox(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.MemberType_var,width=27,state="readonly")
                        comMember['values']=("Admin","Student","Faculty")
                        comMember.grid(row=0,column=1)

                        #PRN NO
                        lblPRN_no=Label(DataFrameLeft,bg="rosy brown",text="PRN Number",font=("time new roman",12,"bold"),padx=2)
                        lblPRN_no.grid(row=1,column=0,sticky=W)
                        txtPRN_no=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.PRN_no_var,width=29)
                        txtPRN_no.grid(row=1,column=1)

                        #Title/ID no
                        lblTitle=Label(DataFrameLeft,bg="rosy brown",text="ID Number",font=("time new roman",12,"bold"),padx=2,pady=4)
                        lblTitle.grid(row=2,column=0,sticky=W)
                        txtTitle=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.Title_var,width=29)
                        txtTitle.grid(row=2,column=1)

                        #FirstName
                        lblFirstName=Label(DataFrameLeft,bg="rosy brown",text="First Name",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblFirstName.grid(row=3,column=0,sticky=W)
                        txtFirstName=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.FirstName_var,width=29)
                        txtFirstName.grid(row=3,column=1)

                        #LastName
                        lblLastName=Label(DataFrameLeft,bg="rosy brown",text="Last Name",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblLastName.grid(row=4,column=0,sticky=W)
                        txtLastName=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.LastName_var,width=29)
                        txtLastName.grid(row=4,column=1)

                        #Address1/City
                        lblAddress1=Label(DataFrameLeft,bg="rosy brown",text="City",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblAddress1.grid(row=5,column=0,sticky=W)
                        txtAddress1=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.Address1_var,width=29)
                        txtAddress1.grid(row=5,column=1)

                        #Address2/state
                        lblAddress2=Label(DataFrameLeft,bg="rosy brown",text="State/Region",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblAddress2.grid(row=6,column=0,sticky=W)
                        txtAddress2=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.Address2_var,width=29)
                        txtAddress2.grid(row=6,column=1)

                        #Post code/Pin
                        lblPostCode=Label(DataFrameLeft,bg="rosy brown",text="Post Code",font=("time new roman",12,"bold"),padx=2,pady=4)
                        lblPostCode.grid(row=7,column=0,sticky=W)
                        txtPostCode=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.PostCode_var,width=29)
                        txtPostCode.grid(row=7,column=1)

                        #Mobile
                        lblMobile=Label(DataFrameLeft,bg="rosy brown",text="Mobile",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblMobile.grid(row=8,column=0,sticky=W)
                        txtMobile=Entry(DataFrameLeft,font=("time new roman",13,"bold"),textvariable=self.Mobile_var,width=29)
                        txtMobile.grid(row=8,column=1)

                        #Book ID
                        lblBookId=Label(DataFrameLeft,bg="rosy brown",text="Book ID",font=("time new roman",12,"bold"),padx=2)
                        lblBookId.grid(row=0,column=2,sticky=W)
                        txtBookId=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.BookID_var,width=29)
                        txtBookId.grid(row=0,column=3)

                        #Book Title
                        lblBookTitle=Label(DataFrameLeft,bg="rosy brown",text="Book Title",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblBookTitle.grid(row=1,column=2,sticky=W)
                        txtBookTitle=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.BookTitle_var,width=29)
                        txtBookTitle.grid(row=1,column=3)

                        #Author Name
                        lblAuthorName=Label(DataFrameLeft,bg="rosy brown",text="Author Name",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblAuthorName.grid(row=2,column=2,sticky=W)
                        txtAuthorName=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.AuthorName_var,width=29)
                        txtAuthorName.grid(row=2,column=3)

                        #Borrowed Date
                        lblBorrowedDate=Label(DataFrameLeft,bg="rosy brown",text="Borrowed Date",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblBorrowedDate.grid(row=3,column=2,sticky=W)
                        txtBorrowedDate=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.BorrowedDate_var,width=29)
                        txtBorrowedDate.grid(row=3,column=3)

                        #Due Date
                        lblDueDate=Label(DataFrameLeft,bg="rosy brown",text="Due Date",font=("time new roman",12,"bold"),padx=2,pady=4)
                        lblDueDate.grid(row=4,column=2,sticky=W)
                        txtDueDate=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.DueDate_var,width=29)
                        txtDueDate.grid(row=4,column=3)

                        #Number Of days
                        lblNoOfDays=Label(DataFrameLeft,bg="rosy brown",text="No. of Days",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblNoOfDays.grid(row=5,column=2,sticky=W)
                        txtNoOfDays=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.NoOfDays_var,width=29)
                        txtNoOfDays.grid(row=5,column=3)

                        #Late Return Fine
                        lblFine=Label(DataFrameLeft,bg="rosy brown",text="Late Return Fine",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblFine.grid(row=6,column=2,sticky=W)
                        txtFine=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.LateReturnFine_var,width=29)
                        txtFine.grid(row=6,column=3)

                        #Date over Due
                        lblOverDue=Label(DataFrameLeft,bg="rosy brown",text="Date Over Due",font=("time new roman",12,"bold"),padx=2,pady=4)
                        lblOverDue.grid(row=7,column=2,sticky=W)
                        txtOverDue=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.DueDate_var,width=29)
                        txtOverDue.grid(row=7,column=3)

                        #Actual Price
                        lblPrice=Label(DataFrameLeft,bg="rosy brown",text="Actual Price",font=("time new roman",12,"bold"),padx=2,pady=6)
                        lblPrice.grid(row=8,column=2,sticky=W)
                        txtPrice=Entry(DataFrameLeft,font=("time new roman",12,"bold"),textvariable=self.ActualPrice_var,width=29)
                        txtPrice.grid(row=8,column=3)

                #===============================================================================================
                #--------------------------DATA FRAME RIGHT---------------------------------------------------#
                        DataFrameRight=LabelFrame(frame,text="Book Details",bg="rosy brown",fg="black",bd=12,relief=RIDGE,
                                                font=("time new roman",15,"bold"),padx=20)
                        DataFrameRight.place(x=905,y=5,width=580,height=350)

                        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=35,height=15,padx=2,pady=6)
                        self.txtBox.grid(row=0,column=2)

                        listScrollBar=Scrollbar(DataFrameRight)
                        listScrollBar.grid(row=0,column=1,sticky="ns")

                        listBooks=["To Kill a Mockingbird","1984","The Great Gatsby","The Catcher in the Rye","Moby-Dick","Pride and Prejudice",
                                "The Lord of the Rings","Jane Eyre","The Hobbit","Fahrenheit 451","Crime and Punishment",
                                "The Adventures of Huckleberry Finn","War and Peace","Wuthering Heights","Brave New World",
                                "Great Expectations","Little Women","Anna Karenina","The Grapes of Wrath","The Picture of Dorian Gray"]
                        

                        def selectBook(event=""):
                                value=str(listBox.get(listBox.curselection()))
                                x=value
                                #book1
                                if (x=="To Kill a Mockingbird"):
                                        self.BookID_var.set("BKID1234")
                                        self.BookTitle_var.set("To Kill a Mockingbird")
                                        self.AuthorName_var.set("Paul Berry")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.700")
                                #book 2
                                elif (x=="1984"):
                                        self.BookID_var.set("BKID2345")
                                        self.BookTitle_var.set("1984")
                                        self.AuthorName_var.set("John Smith")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.780")

                                #book 3
                                elif (x=="The Great Gatsby",):
                                        self.BookID_var.set("BKID3456")
                                        self.BookTitle_var.set("The Great Gatsby",)
                                        self.AuthorName_var.set("Jane Doe")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.600")

                                #book 4
                                if (x=="The Catcher in the Rye"):
                                        self.BookID_var.set("BKID4567")
                                        self.BookTitle_var.set("The Catcher in the Rye")
                                        self.AuthorName_var.set("Michael Johnson")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.560")

                                #book 5
                                if (x=="Moby-Dick"):
                                        self.BookID_var.set("BKID5678")
                                        self.BookTitle_var.set("Moby-Dick")
                                        self.AuthorName_var.set("Emily Davis")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.850")

                                #book 6
                                if (x=="Pride and Prejudice"):
                                        self.BookID_var.set("BKID6789")
                                        self.BookTitle_var.set("Pride and Prejudice")
                                        self.AuthorName_var.set("Robert Brown")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.650")

                                #book 7
                                if (x=="The Lord of the Rings"):
                                        self.BookID_var.set("BKID7890")
                                        self.BookTitle_var.set("The Lord of the Rings")
                                        self.AuthorName_var.set("Jessica Wilson")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.450")

                                #book 8
                                if (x=="Jane Eyre"):
                                        self.BookID_var.set("BKID8901")
                                        self.BookTitle_var.set( "Jane Eyre")
                                        self.AuthorName_var.set("David Anderson")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.950")

                                #book 9
                                if (x=="The Hobbit"):
                                        self.BookID_var.set("BKID9012")
                                        self.BookTitle_var.set("The Hobbit")
                                        self.AuthorName_var.set("Mary Martinez")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.670")

                                #book 10
                                if (x=="Fahrenheit 451"):
                                        self.BookID_var.set("BKID1023")
                                        self.BookTitle_var.set("Fahrenheit 451")
                                        self.AuthorName_var.set("James Thomas")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.900")

                                #book 11
                                if (x=="Crime and Punishment"):
                                        self.BookID_var.set("BKID1145")
                                        self.BookTitle_var.set("Crime and Punishment")
                                        self.AuthorName_var.set("Patricia Garcia")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.720")

                                #book 12
                                if (x=="The Adventures of Huckleberry Finn"):
                                        self.BookID_var.set("BKID1267")
                                        self.BookTitle_var.set("The Adventures of Huckleberry Finn")
                                        self.AuthorName_var.set("Christopher Harris")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.500")

                                #book 13
                                if (x=="War and Peace"):
                                        self.BookID_var.set("BKID1389")
                                        self.BookTitle_var.set("War and Peace")
                                        self.AuthorName_var.set("Linda Clark")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.600")

                                #book 14
                                if (x=="Wuthering Heights"):
                                        self.BookID_var.set("BKID1401")
                                        self.BookTitle_var.set("Wuthering Heights")
                                        self.AuthorName_var.set("Daniel Lewis")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.630")

                                #book 15
                                if (x=="Brave New World"):
                                        self.BookID_var.set("BKID1521")
                                        self.BookTitle_var.set("Brave New World")
                                        self.AuthorName_var.set("Barbara Robinson")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.750")

                                #book 16
                                if (x=="Great Expectations"):
                                        self.BookID_var.set("BKID1632")
                                        self.BookTitle_var.set("Great Expectations")
                                        self.AuthorName_var.set("Matthew Walker")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.680")

                                #book 17
                                if (x=="Little Women"):
                                        self.BookID_var.set("BKID1743")
                                        self.BookTitle_var.set("Little Women")
                                        self.AuthorName_var.set("Jennifer Hall")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.550")

                                #book 18
                                if (x=="Anna Karenina"):
                                        self.BookID_var.set("BKID1854")
                                        self.BookTitle_var.set("Anna Karenina")
                                        self.AuthorName_var.set("Joseph Young")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.520")

                                #book 19
                                if (x=="The Grapes of Wrath"):
                                        self.BookID_var.set("BKID1965")
                                        self.BookTitle_var.set("The Grapes of Wrath")
                                        self.AuthorName_var.set("Charles Scott")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.640")

                                #book 20
                                if (x=="The Picture of Dorian Gray"):
                                        self.BookID_var.set("BKID2087")
                                        self.BookTitle_var.set("The Picture of Dorian Gray")
                                        self.AuthorName_var.set("Susan Adams")

                                        d1=datetime.datetime.today()
                                        d2=datetime.timedelta(days=15)
                                        d3=d1+d2
                                        self.BorrowedDate_var.set(d1)
                                        self.DueDate_var.set(d3)
                                        self.NoOfDays_var.set(15)
                                        self.LateReturnFine_var.set("Rs.50")
                                        self.OverDue_var.set("No")
                                        self.ActualPrice_var.set("Rs.840")                                


                        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
                        listBox.bind("<<ListboxSelect>>",selectBook)

                        listBox.grid(row=0,column=0,padx=4)
                        listScrollBar.config(command=listBox.yview)

                        for item in listBooks:
                                listBox.insert(END,item)

                #=========================================================================================
                #---------------------------Button frame--------------------------------------------------#
                        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="rosy brown")
                        framebutton.place(x=0,y=530,width=1535,height=70)

                        #Add Data Button
                        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=0)

                        #Show Data Button
                        btnAddData=Button(framebutton,command=self.Show_Data,text="Show Data",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=1)

                        #Update Button
                        btnAddData=Button(framebutton,command=self.update,text="Update",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=2)

                        #Delete Button
                        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=3)

                        #Reset Button
                        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=4)

                        #Exit Button
                        btnAddData=Button(framebutton,command=self.iexit,text="Exit",font=("monospace",12,"bold"),width=23,bg="coral3",fg="DarkOrchid4",padx=5,pady=5)
                        btnAddData.grid(row=0,column=5)


                #===========================================================================================
                #-------------------------------------Information frame------------------------------------#
                        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="rosy brown")
                        frameDetails.place(x=0,y=600,width=1535,height=195)

                        Table_Frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="rosy brown")
                        Table_Frame.place(x=0,y=2,width=1480,height=168)

                        xscroll=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
                        yscroll=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

                        self.library_table=ttk.Treeview(Table_Frame,column=("MemberType","PRN_no","Title","FirstName","LastName",
                                                                            "Address1","Address2","Postcode","Mobile","BookId",
                                                                            "BookTitle","AuthorName","Borroweddate","DueDate",
                                                                            "NoOfdays","LateReturnFine","OverDue","Price")
                                                ,xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

                        xscroll.pack(side=BOTTOM,fill=X)
                        yscroll.pack(side=RIGHT,fill=Y)
                        xscroll.config(command=self.library_table.xview)
                        yscroll.config(command=self.library_table.yview)


                        self.library_table.heading("MemberType",text="Member Type")
                        self.library_table.heading("PRN_no",text="PRN No")
                        self.library_table.heading("Title",text="ID Number")
                        self.library_table.heading("FirstName",text="First Name")
                        self.library_table.heading("LastName",text="Last Name")
                        self.library_table.heading("Address1",text="City")
                        self.library_table.heading("Address2",text="Region")
                        self.library_table.heading("Postcode",text="Postcode")
                        self.library_table.heading("Mobile",text="Mobile")
                        self.library_table.heading("BookId",text="Book Id")
                        self.library_table.heading("BookTitle",text="Book Title")
                        self.library_table.heading("AuthorName",text="Author Name")
                        self.library_table.heading("Borroweddate",text="Borrowed Date")
                        self.library_table.heading("DueDate",text="Due Date")
                        self.library_table.heading("NoOfdays",text="No Of Days")
                        self.library_table.heading("LateReturnFine",text="Late Return Fine")
                        self.library_table.heading("OverDue",text="Date Over Due")
                        self.library_table.heading("Price",text="Actual Price")
                                                
                        self.library_table["show"]="headings"
                        self.library_table.pack(fill=BOTH,expand=1)

                        self.library_table.column("MemberType",width=100)
                        self.library_table.column("PRN_no",width=100)
                        self.library_table.column("Title",width=100)
                        self.library_table.column("FirstName",width=100)
                        self.library_table.column("LastName",width=100)
                        self.library_table.column("Address1",width=100)
                        self.library_table.column("Address2",width=100)
                        self.library_table.column("Postcode",width=100)
                        self.library_table.column("Mobile",width=100)
                        self.library_table.column("BookId",width=100)
                        self.library_table.column("BookTitle",width=100)
                        self.library_table.column("AuthorName",width=100)
                        self.library_table.column("Borroweddate",width=100)
                        self.library_table.column("DueDate",width=100)
                        self.library_table.column("NoOfdays",width=100)
                        self.library_table.column("LateReturnFine",width=100)
                        self.library_table.column("OverDue",width=100)
                        self.library_table.column("Price",width=100)

                        self.fetch_data()
                        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



         #--------------------ADD FUNCTION------------------------------------------------------------
                def add_data(self):
                        conn=mysql.connector.connect(user='root',
                                                    password='your_password',
                                                    host='localhost', 
                                                    database='mydata')
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                   ,(   self.MemberType_var.get(),
                                                        self.PRN_no_var.get(),
                                                        self.Title_var.get(),
                                                        self.FirstName_var.get(),
                                                        self.LastName_var.get(),
                                                        self.Address1_var.get(),
                                                        self.Address2_var.get(),
                                                        self.PostCode_var.get(),
                                                        self.Mobile_var.get(),
                                                        self.BookID_var.get(),
                                                        self.BookTitle_var.get(),
                                                        self.AuthorName_var.get(),
                                                        self.BorrowedDate_var.get(),
                                                        self.DueDate_var.get(),
                                                        self.NoOfDays_var.get(),
                                                        self.LateReturnFine_var.get(),
                                                        self.OverDue_var.get(),
                                                        self.ActualPrice_var.get()
                                        ))
                        
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Member has been inserted successfully.")

        #------UPDATE FUNCTION----------------------------------------------------------------
                def update(self):
                        conn=mysql.connector.connect(user='root',password='your_password',host='localhost', database='mydata')
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update library set MemberType=%s,Title=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,BookID=%s,BookTitle=%s,AuthorName=%s,BorrowedDate=%s,DueDate=%s,NoOfDays=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_No=%s",(
                                self.MemberType_var.get(),
                                self.Title_var.get(),
                                self.FirstName_var.get(),
                                self.LastName_var.get(),
                                self.Address1_var.get(),
                                self.Address2_var.get(),
                                self.PostCode_var.get(),
                                self.Mobile_var.get(),
                                self.BookID_var.get(),
                                self.BookTitle_var.get(),
                                self.AuthorName_var.get(),
                                self.BorrowedDate_var.get(),
                                self.DueDate_var.get(),
                                self.NoOfDays_var.get(),
                                self.LateReturnFine_var.get(),
                                self.OverDue_var.get(),
                                self.ActualPrice_var.get(),
                                self.PRN_no_var.get()
                                ))
                        conn.commit()
                        self.fetch_data()
                        self.reset()
                        conn.close()
                
                        messagebox.showinfo("Success","Member has been updated successfully.")

                #-----------------------FETCH DATA FUNCTION---------------------------------------------
                def fetch_data(self):
                        conn=mysql.connector.connect(user='root',password='your_password',host='localhost', database='mydata')
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from library")
                        rows=my_cursor.fetchall()
                        if len(rows)!=0:
                                self.library_table.delete(*self.library_table.get_children())
                                for i in rows:
                                        self.library_table.insert("",END,values=i)
                                conn.commit()
                        conn.close()
                                
                def get_cursor(self,event=""):
                        cursor_row=self.library_table.focus()
                        content=self.library_table.item(cursor_row)
                        row=content['values']
                        self.MemberType_var.set(row[0])
                        self.PRN_no_var.set(row[1])
                        self.Title_var.set(row[2])
                        self.FirstName_var.set(row[3])
                        self.LastName_var.set(row[4])
                        self.Address1_var.set(row[5])
                        self.Address2_var.set(row[6])
                        self.PostCode_var.set(row[7])
                        self.Mobile_var.set(row[8])
                        self.BookID_var.set(row[9])
                        self.BookTitle_var.set(row[10])
                        self.AuthorName_var.set(row[11])
                        self.BorrowedDate_var.set(row[12])
                        self.DueDate_var.set(row[13])
                        self.NoOfDays_var.set(row[14])
                        self.LateReturnFine_var.set(row[15])
                        self.OverDue_var.set(row[16])
                        self.ActualPrice_var.set(row[17])

                #------------------------SHOW DATA FUNCTION----------------------------------------------------
                def Show_Data(self):
                        self.txtBox.insert(END,"Member Type\t\t" + self.MemberType_var.get() + "\n")
                        self.txtBox.insert(END,"PRN No.\t\t" + self.PRN_no_var.get() + "\n")
                        self.txtBox.insert(END,"Title\t\t" + self.Title_var.get() + "\n")
                        self.txtBox.insert(END,"First Name\t\t" + self.FirstName_var.get() + "\n")
                        self.txtBox.insert(END,"Last Name\t\t" + self.LastName_var.get() + "\n")
                        self.txtBox.insert(END,"Address1\t\t" + self.Address1_var.get() + "\n")
                        self.txtBox.insert(END,"Address2\t\t" + self.Address2_var.get() + "\n")
                        self.txtBox.insert(END,"Post Code\t\t" + self.PostCode_var.get() + "\n")
                        self.txtBox.insert(END,"Mobile\t\t" + self.Mobile_var.get() + "\n")
                        self.txtBox.insert(END,"Book ID\t\t" + self.BookID_var.get() + "\n")
                        self.txtBox.insert(END,"Book Title\t\t" + self.BookTitle_var.get() + "\n")
                        self.txtBox.insert(END,"Author Name\t\t" + self.AuthorName_var.get() + "\n")
                        self.txtBox.insert(END,"Borrowed Date\t\t" + self.BorrowedDate_var.get() + "\n")
                        self.txtBox.insert(END,"Due Date\t\t" + self.DueDate_var.get() + "\n")
                        self.txtBox.insert(END,"No Of Days\t\t" + self.NoOfDays_var.get() + "\n")
                        self.txtBox.insert(END,"Late Return Fine\t\t" + self.LateReturnFine_var.get() + "\n")
                        self.txtBox.insert(END,"Over Due\t\t" + self.OverDue_var.get() + "\n")
                        self.txtBox.insert(END,"Actual Price\t\t" + self.ActualPrice_var.get() + "\n")

                #--------------------------RESET FUNCTION----------------------------------------------
                def reset(self):
                        self.MemberType_var.set(""),
                        self.PRN_no_var.set(""),
                        self.Title_var.set(""),
                        self.FirstName_var.set(""),
                        self.LastName_var.set(""),
                        self.Address1_var.set(""),
                        self.Address2_var.set(""),
                        self.PostCode_var.set(""),
                        self.Mobile_var.set(""),
                        self.BookID_var.set(""),
                        self.BookTitle_var.set(""),
                        self.AuthorName_var.set(""),
                        self.BorrowedDate_var.set(""),
                        self.DueDate_var.set(""),
                        self.NoOfDays_var.set(""),
                        self.LateReturnFine_var.set(""),
                        self.OverDue_var.set(""),
                        self.ActualPrice_var.set("")
                        self.txtBox.delete("1.0",END)

                #-----------------------EXIT FUNCTION--------------------------------------------------------
                def iexit(self):
                        iexit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
                        if iexit>0:
                                self.root.destroy()
                                return

                #------------------------DELETE FUNCTION-------------------------------------------------------
                def delete(self):
                        if self.PRN_no_var.get()=="" or self.Title_var.get()=="":
                                messagebox.showerror("Error","First select the Member")
                        else:
                                conn=mysql.connector.connect(user='root',password='your_password',host='localhost', database='mydata')
                                my_cursor=conn.cursor()
                                query="delete from library where PRN_no=%s"
                                value=(self.PRN_no_var.get(),)
                                my_cursor.execute(query,value)
                                conn.commit()
                                self.fetch_data()
                                self.reset()
                                conn.close()

                                messagebox.showinfo("Success","Member has been deleted")


#================================MAIN FUNCTION============================================
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()