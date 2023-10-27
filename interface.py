from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Students
from train_data import Train_Data
from face_recognition import Face_Recognition
import os


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(r"Img\OMB-AI-Blog-Image_06.08.23-scaled.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=800)

        title_lbl = Label(
            bg_img,
            text="Facial Attendance System",
            font=("sans serif", 35, "bold"),
            bg="dark blue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=750, height=60)

        img2 = Image.open(
            r"Img\cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L2FpMjQwODIzLTNkLXJlbWl4LWhpLTAwNy5qcGc.webp"
        )
        img2 = img2.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        student_button = Button(
            bg_img, image=self.photoimg2, cursor="hand2", command=self.students_details
        )
        student_button.place(x=70, y=120, width=220, height=220)

        student_button_1 = Button(
            bg_img,
            text="Student Details",
            cursor="hand2",
            command=self.students_details,
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        student_button_1.place(x=70, y=350, width=220, height=40)

        img3 = Image.open(r"Img\blue color-min-1.png")
        img3 = img3.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        facial_recognition_button = Button(
            bg_img,
            image=self.photoimg3,
            cursor="hand2",
            command=self.face_recognition_page,
        )
        facial_recognition_button.place(x=350, y=120, width=220, height=220)

        facial_recognition_button_1 = Button(
            bg_img,
            command=self.face_recognition_page,
            text="Face Recognition",
            cursor="hand2",
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        facial_recognition_button_1.place(x=350, y=350, width=220, height=40)

        img4 = Image.open(r"Img\GettyImages-1198430065.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        attendance_button = Button(bg_img, image=self.photoimg4, cursor="hand2")
        attendance_button.place(x=630, y=120, width=220, height=220)

        attendance_button_1 = Button(
            bg_img,
            text="Attendance",
            cursor="hand2",
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        attendance_button_1.place(x=630, y=350, width=220, height=40)

        img5 = Image.open(r"Img\big-data.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        training_data_button = Button(
            bg_img,
            image=self.photoimg5,
            cursor="hand2",
            command=self.data_training_page,
        )
        training_data_button.place(x=70, y=420, width=220, height=220)

        training_data_button_1 = Button(
            bg_img,
            text="Data Training",
            command=self.data_training_page,
            cursor="hand2",
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        training_data_button_1.place(x=70, y=650, width=220, height=40)

        img6 = Image.open(
            r"Img\gallery-minimal-vector-line-icon-3d-button-isolated-black-background-premium-vector_570929-1676.jpg"
        )
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        picture_button = Button(
            bg_img, image=self.photoimg6, cursor="hand2", command=self.picture_page
        )
        picture_button.place(x=350, y=420, width=220, height=220)

        picture_button_1 = Button(
            bg_img,
            command=self.picture_page,
            text="Pictures",
            cursor="hand2",
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        picture_button_1.place(x=350, y=650, width=220, height=40)

        img7 = Image.open(r"Img\power-button-computer-laptop-featured.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        exit_button = Button(bg_img, image=self.photoimg7, cursor="hand2")
        exit_button.place(x=630, y=420, width=220, height=220)

        exit_button_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            font=("sans serif", 15, "bold"),
            bg="royal blue",
            fg="white",
        )
        exit_button_1.place(x=630, y=650, width=220, height=40)

    def students_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Students(self.new_window)

    def picture_page(self):
        os.startfile("data")

    def data_training_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_Data(self.new_window)

    def face_recognition_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Interface(root)
    root.mainloop()
