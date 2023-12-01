from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import os
from datetime import datetime
from tkinter import filedialog

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        self.var_search = StringVar()

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # ===============Images==================================

        # image1
        img10 = Image.open(r"college_images\1st.jpg")
        img10 = img10.resize((510, 160), Image.LANCZOS)

        self.photoImg10 = ImageTk.PhotoImage(img10)

        self.f_lbl_1 = Button(self.root, command=self.openImg_1, image=self.photoImg10, cursor="hand2")
        self.f_lbl_1.place(x=(-10), y=0, width=545, height=160)

        # image2
        img11 = Image.open(r"college_images\2nd.jpg")
        img11 = img11.resize((500, 160), Image.LANCZOS)
        self.photoImg11 = ImageTk.PhotoImage(img11)

        self.f_lbl_2 = Button(self.root, command=self.openImg_2, image=self.photoImg11, cursor="hand2")
        self.f_lbl_2.place(x=515, y=0, width=500, height=160)

        # image3
        img13 = Image.open(r"college_images\student.jpg")
        img13 = img13.resize((550, 160), Image.LANCZOS)
        self.photoImg13 = ImageTk.PhotoImage(img13)

        self.f_lbl_3 = Button(self.root, command=self.openImg_3, image=self.photoImg13, cursor="hand2")
        self.f_lbl_3.place(x=990, y=0, width=550, height=160)

        # ====================Background image==============================================
        img1 = Image.open(r"college_images\university.jpg")
        img1 = img1.resize((1535, 710), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl = Label(self.root, image=self.photoImg1, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=130, width=1535, height=710)

        Manage_std_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_std_frame.place(x=15, y=55, width=1500, height=600)

        # ==================== Project title ==================================================
        title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 37, "bold"), bg="white",
                      fg="blue")
        title.place(x=0, y=(-2), width=1550, height=50)

        img_logo = Image.open(r"college_images\logo.png")
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)
        self.photoImg_logo = ImageTk.PhotoImage(img_logo)
        bg_lbl = Label(bg_lbl, image=self.photoImg_logo, bd=20)
        bg_lbl.place(x=300, y=2, width=50, height=40)

        # =================time================================
        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title, font=('times new roman', 16, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=(-15), width=120, height=50)
        time()

        # =======Framedetails===================================================================================

        DataFrameLeft = LabelFrame(Manage_std_frame, bd=4, padx=2, relief=RIDGE, fg="crimson", bg="white",
                                    font=("arial", 12, "bold"), text="Student Information ")
        DataFrameLeft.place(x=10, y=10, width=660, height=580)

        # ================Right labelframe=================
        DataFrameRight = LabelFrame(Manage_std_frame, bd=4, padx=2, relief=RIDGE, bg="white", fg="crimson",
                                     font=("arial", 12, "bold"), text="Student Details")
        DataFrameRight.place(x=670, y=10, width=820, height=580)

        img30 = Image.open(r"college_images\8th.jpg")
        img30 = img30.resize((650, 120), Image.LANCZOS)
        self.photoImg30 = ImageTk.PhotoImage(img30)
        myimg = Label(DataFrameLeft, image=self.photoImg30, bd=2, relief=RIDGE)
        myimg.place(x=0, y=(-3), width=650, height=120)

        img20 = Image.open(r"college_images\3rd.jpg")
        img20 = img20.resize((810, 200), Image.LANCZOS)
        self.photoImg20 = ImageTk.PhotoImage(img20)
        bg_lbl = Label(DataFrameRight, image=self.photoImg20)
        bg_lbl.place(x=0, y=0, width=810, height=200)

        # Curent course Information labelFrame
        std_Info_label_frame = LabelFrame(DataFrameLeft, padx=10, bd=2, relief=RIDGE,
                                          font=("times new roman", 11, "bold"), fg="darkgreen", bg="white",
                                          text="Current Course Information")
        std_Info_label_frame.place(x=1, y=100, width=650, height=115)

        # label and entries
        # department
        lbl_dep = Label(std_Info_label_frame, font=("arial", 12, "bold"), text="Department:", bg="white")
        lbl_dep.grid(row=0, column=0, sticky=W, padx=2, pady=10)
        com_dep = ttk.Combobox(std_Info_label_frame, textvariable=self.var_dep, state="readonly",
                               font=("arial", 12, "bold"), width=17)
        com_dep['value'] = ("Select Department", "Computer", "Mechnical", "Civil", "Electonic", "Electrical",
                            "Automobile", "IT")
        com_dep.current(0)
        com_dep.grid(row=0, column=1, sticky=W, padx=2)

        # course
        course_std = Label(std_Info_label_frame, font=("arial", 12, "bold"), text="Courses:", bg="white")
        course_std.grid(row=0, column=2, sticky=W, padx=2, pady=10)
        com_course = ttk.Combobox(std_Info_label_frame, textvariable=self.var_course, state="readonly",
                                  font=("arial", 12, "bold"), width=17)
        com_course['value'] = ("Select Course", "FE", "SE", "TE", "BE")
        com_course.current(0)
        com_course.grid(row=0, column=3, sticky=W, padx=2)

        # Year
        lbl_year = Label(std_Info_label_frame, font=("arial", 12, "bold"), text="Year:", bg="white")
        lbl_year.grid(row=1, column=0, sticky=W, padx=2, pady=10)
        com_year = ttk.Combobox(std_Info_label_frame, textvariable=self.var_year, state="readonly",
                                font=("arial", 12, "bold"), width=17)
        com_year['value'] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        com_year.current(0)
        com_year.grid(row=1, column=1, sticky=W, padx=2)

        # Semester
        lbl_semester = Label(std_Info_label_frame, font=("arial", 12, "bold"), text="Semester:", bg="white")
        lbl_semester.grid(row=1, column=2, sticky=W, padx=2, pady=10)
        com_semester = ttk.Combobox(std_Info_label_frame, textvariable=self.var_semester, state="readonly",
                                    font=("arial", 12, "bold"), width=17)
        com_semester['value'] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7",
                                "Sem-8")
        com_semester.current(0)
        com_semester.grid(row=1, column=3, sticky=W, padx=2)

        # ============================================================================================================

        # Class Student Information
        class_Student_label_frame = LabelFrame(DataFrameLeft, padx=2, relief=RIDGE,
                                               font=("times new roman", 12, "bold"), fg="darkgreen", bg="white",
                                               text="Student Class Details")
        class_Student_label_frame.place(x=1, y=215, width=650, height=250)

        # student Id
        lbl_studentId = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Student Id:", bg="white")
        lbl_studentId.grid(row=0, column=0, sticky=W, padx=2, pady=1)
        entry_studentId = ttk.Entry(class_Student_label_frame, textvariable=self.va_std_id, width=20,
                                   font=("arial", 12, "bold"))
        entry_studentId.grid(row=0, column=1, padx=2, pady=1)

        # student name
        lbl_studentName = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Student Name:", bg="white")
        lbl_studentName.grid(row=0, column=2, sticky=W, padx=2, pady=1)
        entry_studentName = ttk.Entry(class_Student_label_frame, textvariable=self.var_std_name, width=20,
                                     font=("arial", 12, "bold"))
        entry_studentName.grid(row=0, column=3, padx=2, pady=1)

        # student roll
        lbl_roll = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Roll No:", bg="white")
        lbl_roll.grid(row=0, column=4, sticky=W, padx=2, pady=1)
        entry_roll = ttk.Entry(class_Student_label_frame, textvariable=self.var_roll, width=20,
                              font=("arial", 12, "bold"))
        entry_roll.grid(row=0, column=5, padx=2, pady=1)

        # student gender
        lbl_gender = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.grid(row=1, column=0, sticky=W, padx=2, pady=1)
        entry_gender = ttk.Combobox(class_Student_label_frame, textvariable=self.var_gender, state="readonly",
                                    font=("arial", 12, "bold"), width=18)
        entry_gender['value'] = ("Male", "Female", "Other")
        entry_gender.grid(row=1, column=1, padx=2, pady=1)

        # student dob
        lbl_dob = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="D.O.B:", bg="white")
        lbl_dob.grid(row=1, column=2, sticky=W, padx=2, pady=1)
        entry_dob = ttk.Entry(class_Student_label_frame, textvariable=self.var_dob, width=20, font=("arial", 12, "bold"))
        entry_dob.grid(row=1, column=3, padx=2, pady=1)

        # student email
        lbl_email = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Email:", bg="white")
        lbl_email.grid(row=1, column=4, sticky=W, padx=2, pady=1)
        entry_email = ttk.Entry(class_Student_label_frame, textvariable=self.var_email, width=20, font=("arial", 12, "bold"))
        entry_email.grid(row=1, column=5, padx=2, pady=1)

        # student contact
        lbl_phone = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Contact No:", bg="white")
        lbl_phone.grid(row=2, column=0, sticky=W, padx=2, pady=1)
        entry_phone = ttk.Entry(class_Student_label_frame, textvariable=self.var_phone, width=20, font=("arial", 12, "bold"))
        entry_phone.grid(row=2, column=1, padx=2, pady=1)

        # student address
        lbl_address = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Address:", bg="white")
        lbl_address.grid(row=2, column=2, sticky=W, padx=2, pady=1)
        entry_address = ttk.Entry(class_Student_label_frame, textvariable=self.var_address, width=20, font=("arial", 12, "bold"))
        entry_address.grid(row=2, column=3, padx=2, pady=1)

        # student teacher
        lbl_teacher = Label(class_Student_label_frame, font=("arial", 12, "bold"), text="Teacher:", bg="white")
        lbl_teacher.grid(row=2, column=4, sticky=W, padx=2, pady=1)
        entry_teacher = ttk.Entry(class_Student_label_frame, textvariable=self.var_teacher, width=20, font=("arial", 12, "bold"))
        entry_teacher.grid(row=2, column=5, padx=2, pady=1)

        # Radio Buttons
        self.var_radio1 = StringVar()
        r1 = ttk.Radiobutton(class_Student_label_frame, variable=self.var_radio1, text="Take Photo Sample",
                            value="Yes")
        r1.grid(row=3, column=0)

        r2 = ttk.Radiobutton(class_Student_label_frame, variable=self.var_radio1, text="No Photo Sample",
                            value="No")
        r2.grid(row=3, column=1)

        # Buttons Frame
        btn_frame = Frame(class_Student_label_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=170, width=635, height=30)

        # Save Button
        savebtn = Button(btn_frame, text="Save", command=self.add_data, font=("arial", 12, "bold"), bg="blue",
                         fg="white", width=18)
        savebtn.grid(row=0, column=0)

        # Update Button
        updatebtn = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 12, "bold"), bg="blue",
                           fg="white", width=18)
        updatebtn.grid(row=0, column=1)

        # Delete Button
        deletebtn = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), bg="blue",
                           fg="white", width=18)
        deletebtn.grid(row=0, column=2)

        # Reset Button
        resetbtn = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 12, "bold"), bg="blue",
                          fg="white", width=18)
        resetbtn.grid(row=0, column=3)

        # Take Photo Button
        take_photobtn = Button(btn_frame, text="Take Photo Sample", command=self.generate_dataset, font=("arial", 12, "bold"),
                               bg="blue", fg="white", width=18)
        take_photobtn.grid(row=0, column=4)

        # Update Photo Button
        update_photobtn = Button(btn_frame, text="Update Photo", font=("arial", 12, "bold"), bg="blue", fg="white",
                                width=18, command=self.update_data)
        update_photobtn.grid(row=0, column=5)

        # Right frame

        # Right frame
        DataFrameRight = LabelFrame(root, bd=1, relief=RIDGE, padx=5, text="Student Details",
                                    fg="darkgreen", font=("times new roman", 12, "bold"), bg="white")
        DataFrameRight.place(x=680, y=5, width=700, height=490)

        # search frame

        SearchFrame = LabelFrame(DataFrameRight, bd=2, relief=RIDGE, padx=20, text="Search System",
                                fg="darkgreen", font=("times new roman", 12, "bold"), bg="white")
        SearchFrame.place(x=5, y=5, width=690, height=70)

        # Search label
        lbl_search = Label(SearchFrame, text="Search By:", font=("arial", 12, "bold"), bg="red")
        lbl_search.grid(row=0, column=0, sticky=W)

        # Search combo box
        self.var_com_search = StringVar()
        com_search = ttk.Combobox(SearchFrame, textvariable=self.var_com_search, state="readonly",
                                  font=("arial", 12, "bold"), width=12)
        com_search['value'] = ("Select", "Roll No", "Phone No")
        com_search.grid(row=0, column=1, padx=2, pady=5)
        com_search.current(0)

        # Search entry
        entry_search = ttk.Entry(SearchFrame, textvariable=self.var_search, width=12, font=("arial", 12, "bold"))
        entry_search.grid(row=0, column=2, padx=2, pady=5)

        # search button
        searchbtn = Button(SearchFrame, text="Search", command=self.search_data, font=("arial", 12, "bold"), bg="blue",
                           fg="white", width=12)
        searchbtn.grid(row=0, column=3, padx=1)

        # show all button
        showallbtn = Button(SearchFrame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"),
                            bg="blue", fg="white", width=12)
        showallbtn.grid(row=0, column=4, padx=1)

        # Table frame

        TableFrame = Frame(DataFrameRight, bd=2, relief=RIDGE, bg="white")
        TableFrame.place(x=5, y=80, width=690, height=400)

        # scroll bar
        scroll_x = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        # student table
        self.student_table = ttk.Treeview(TableFrame, column=(
        "dep", "course", "year", "semester", "id", "name", "roll", "gender", "dob", "email", "phone", "address", "teacher",
        "photo"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table['show'] = "headings"

        # set the width
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        # Pack the table
        self.student_table.pack(fill=BOTH, expand=1)

        # Fetch data
        self.fetch_data()

        # add student details
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        # =======================================================================================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.va_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.va_std_id.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get()
                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", "end", values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.va_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOb=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where ID=%s",
                                      (self.var_dep.get(),
                                       self.var_course.get(),
                                       self.var_year.get(),
                                       self.var_semester.get(),
                                       self.var_std_name.get(),
                                       self.var_div.get(),
                                       self.var_roll.get(),
                                       self.var_gender.get(),
                                       self.var_dob.get(),
                                       self.var_email.get(),
                                       self.var_phone.get(),
                                       self.var_address.get(),
                                       self.var_teacher.get(),
                                       self.va_std_id.get()
                                       ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted the student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set("")

    def openImg_1(self):
        os.startfile("data")

    def openImg_2(self):
        os.startfile("data")

    def openImg_3(self):
        os.startfile("data")

    def search_data(self):
        if self.var_com_search.get() == "Select" or self.var_search.get() == "":
            messagebox.showerror("Error", "Select combo option and enter search entry", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    f"select * from student where {str(self.var_com_search.get())} LIKE '%{str(self.var_search.get())}%'")
                rows = my_cursor.fetchall()
                if len(rows) == 0:
                    messagebox.showerror("Error", "Data not found", parent=self.root)
                else:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", "end", values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.va_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="employee1")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where ID=%s",
                                  (
                                  self.var_std_name.get(),
                                  self.var_div.get(),
                                  self.var_roll.get(),
                                  self.var_gender.get(),
                                  self.var_dob.get(),
                                  self.var_email.get(),
                                  self.var_phone.get(),
                                  self.var_address.get(),
                                  self.var_teacher.get(),
                                  self.va_std_id.get() == ""
                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                cam = cv2.VideoCapture(0)
                harcascadePath = "haarcascade_frontalface_default.xml"
                face_cascade = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0

                while True:
                    if (sampleNum) > 60:
                        break
                    ret, frame = cam.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        sampleNum = sampleNum + 1
                        cv2.imwrite("data" + os.sep + "User." + str(id) + "." + self.va_std_id.get() + '.' + str(
                            sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                        cv2.imshow('Frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root = mainloop()
