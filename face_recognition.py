from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="Face Recognition",
            font=("sans serif", 35, "bold"),
            bg="dark blue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1535, height=60)

        img1 = Image.open(
            r"Img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.webp"
        )
        img1 = img1.resize((1600, 800), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=60, width=1600, height=750)

        face_recognizer_btn = Button(
            bg_img,
            text="Face Recognition",
            command=self.face_recog,
            cursor="hand2",
            font=("sans serif", 18, "bold"),
            bg="black",
            fg="white",
            borderwidth=0,
        )
        face_recognizer_btn.place(x=670, y=650, width=230, height=60)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, txt, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbours
            )

            coordinates = []
            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="december/4/2005",
                    database="face_recognition_system",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_Id=" + str(id)
                )
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_Id=" + str(id)
                )
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Department from student where Student_Id=" + str(id)
                )
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 85:
                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                coordinates = [x, y, w, h]
            return coordinates

        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
