from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(
            r"C:\Users\SaadAliKhan\Desktop\facial_recognition_system\Img\OMB-AI-Blog-Image_06.08.23-scaled.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=800)

        title_lbl = Label(bg_img, text="Student Management System", font=("sans serif", 35, "bold"), bg="dark blue",
                          fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0, y=60, width=1920, height=730)

        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Data",font=("sans serif",18,"bold"),bg="white")
        left_frame.place(x=20, y=10, width=730, height=700)

        img_left = Image.open(r"C:\Users\SaadAliKhan\Desktop\facial_recognition_system\Img\nedpic.jpg")
        img_left = img_left.resize((800, 205), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_img = Label(left_frame, image=self.photoimg_left)
        left_img.place(x=5, y=0, width=720, height=200)

        # Course Information

        course_info_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Course Information",font=("sans serif",16,"bold"),bg="white")
        course_info_frame.place(x=5, y=210, width=715, height=120)

        # department

        department_label = Label(course_info_frame, text="Department:",font=("sans serif",12,"bold"),bg="white")
        department_label.grid(row=0,column=0,padx=10,sticky=W)

        select_combo = ttk.Combobox(course_info_frame, font=("sans serif",12), state="readonly",width=20)
        select_combo["values"] = ("Select Department", "Software Engineering", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering", "Chemical Engineering")
        select_combo.current(0)
        select_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course

        course_label = Label(course_info_frame, text="Course:",font=("sans serif",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        select_combo = ttk.Combobox(course_info_frame, font=("sans serif",12), state="readonly",width=20)
        select_combo["values"] = ("Select Course", "PL", "CALCULUS", "FIT", "PST", "FE","OHS")
        select_combo.current(0)
        select_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year

        year_label = Label(course_info_frame, text="Year:",font=("sans serif",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        select_combo = ttk.Combobox(course_info_frame, font=("sans serif",12), state="readonly",width=20)
        select_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        select_combo.current(0)
        select_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label = Label(course_info_frame, text="Semester:",font=("sans serif",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        select_combo = ttk.Combobox(course_info_frame, font=("sans serif",12), state="readonly",width=20)
        select_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5","6","7","8")
        select_combo.current(0)
        select_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student Information

        student_info_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Student Information",font=("sans serif", 16, "bold"), bg="white")
        student_info_frame.place(x=5, y=330, width=715, height=330)

        # Student ID

        student_id_label = Label(student_info_frame, text="Student Id:", font=("sans serif", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        student_id_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_id_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)

        # Student name

        student_name_label = Label(student_info_frame, text="Student Name:", font=("sans serif", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        student_name_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_name_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        # Student section

        student_section_label = Label(student_info_frame, text="Student Section:", font=("sans serif", 12, "bold"), bg="white")
        student_section_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        student_section_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_section_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)

        # Student roll no

        student_roll_no_label = Label(student_info_frame, text="Roll No:", font=("sans serif", 12, "bold"), bg="white")
        student_roll_no_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        student_roll_no_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_roll_no_entry.grid(row=1, column=3, padx=10,pady=5, sticky=W)

        # Gender

        student_gender_label = Label(student_info_frame, text="Gender:", font=("sans serif", 12, "bold"), bg="white")
        student_gender_label.grid(row=2, column=0, padx=10,pady=5, sticky=W)

        student_gender_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_gender_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)

        # DOB

        student_dob_label = Label(student_info_frame, text="Date of Birth:", font=("sans serif", 12, "bold"), bg="white")
        student_dob_label.grid(row=2, column=2, padx=10,pady=5, sticky=W)

        student_dob_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_dob_entry.grid(row=2, column=3, padx=10,pady=5, sticky=W)

        # Email

        student_email_label = Label(student_info_frame, text="Email:", font=("sans serif", 12, "bold"), bg="white")
        student_email_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        student_email_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_email_entry.grid(row=3, column=1, padx=10,pady=5, sticky=W)

        # Phone

        student_phone_no_label = Label(student_info_frame, text="Phone No:", font=("sans serif", 12, "bold"), bg="white")
        student_phone_no_label.grid(row=3, column=2, padx=10,pady=5, sticky=W)

        student_phone_no_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_phone_no_entry.grid(row=3, column=3, padx=10,pady=5, sticky=W)

        # Address

        student_address_label = Label(student_info_frame, text="Address:", font=("sans serif", 12, "bold"), bg="white")
        student_address_label.grid(row=4, column=0, padx=10,pady=5, sticky=W)

        student_address_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_address_entry.grid(row=4, column=1, padx=10,pady=5, sticky=W)

        # Teacher

        student_teacher_label = Label(student_info_frame, text="Teacher Name:", font=("sans serif", 12, "bold"), bg="white")
        student_teacher_label.grid(row=4, column=2, padx=10,pady=5, sticky=W)

        student_teacher_entry = ttk.Entry(student_info_frame,width=20, font=("sans serif", 12))
        student_teacher_entry.grid(row=4, column=3, padx=10,pady=5, sticky=W)

        # Radio Buttons

        radio_btn1 = ttk.Radiobutton(student_info_frame,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=6,column=0)
        radio_btn2 = ttk.Radiobutton(student_info_frame,text="No Photo Sample",value="No")
        radio_btn2.grid(row=6,column=1)

        # Buttons Frame

        btn_frame_1 = Frame(student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame_1.place(x=5,y=210,width=700,height=40)

        save_btn = Button(btn_frame_1,text="Save",width=17,font=("sans serif",13,"bold"),bg="royal blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame_1,text="Update",width=16,font=("sans serif",13,"bold"),bg="dark blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame_1,text="Delete",width=16,font=("sans serif",13,"bold"),bg="royal blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame_1,text="Reset",width=17,font=("sans serif",13,"bold"),bg="dark blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame_2 = Frame(student_info_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame_2.place(x=5, y=255, width=700, height=40)

        take_photo_btn = Button(btn_frame_2,text="Take Photo Sample",width=34,font=("sans serif",13,"bold"),bg="royal blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame_2,text="Update Photo Sample",width=34,font=("sans serif",13,"bold"),bg="dark blue",fg="white")
        update_photo_btn.grid(row=1,column=2)

        # Right Frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Data",font=("sans serif",18,"bold"),bg="white")
        right_frame.place(x=780, y=10, width=730, height=700)





if __name__ == "__main__":
    root = Tk()
    obj = Interface(root)
    root.mainloop()
