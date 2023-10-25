from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train_Data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="Training Data Set",
            font=("sans serif", 35, "bold"),
            bg="dark blue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1535, height=60)

        img1 = Image.open(r"Img\ozadje2.jpg")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=60, width=1550, height=740)

        train_data_btn = Button(
            bg_img,
            text="Train Data",
            command=self.data_trainer,
            cursor="hand2",
            font=("sans serif", 24, "bold"),
            bg="black",
            fg="white",
            borderwidth=0,
        )
        train_data_btn.place(x=-5, y=350, width=1550, height=60)

    def data_trainer(self):
        data_dir = "data"
        # list comprehension
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Gray Scale
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Training Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train_Data(root)
    root.mainloop()
