from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from interface import Interface

class Facial_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(r"C:\Users\SaadAliKhan\Desktop\facial_recognition_system\Img\secure-attendance-system.png")
        img1 = img1.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        main_img = Label(self.root, image=self.photoimg1)
        main_img.place(x=0, y=0, width=1550, height=800)

        click_lbl = Button(main_img, text="Click Here",command=self.interface_page, font=("sans serif", 35, "bold"), bg="royal blue", fg="white", cursor="hand2")
        click_lbl.place(x=1000, y=700, width=250, height=50)



    def interface_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Interface(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Facial_Recognition_System(root)
    root.mainloop()
