#---------------change this #User#Root:#123 by replace all other parameters like it in each python file------------------

from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import loginAdmin
import AboutUs
import loginTeacher
import student432

class Main_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("منظومة تنزيل المواد")
        self.root.geometry('500x500+800+100')
        self.root.resizable(False, False)
        
        self.inter = StringVar()
        self.passinter = StringVar()

        self.setup_ui()

    def setup_ui(self):

        self.root.config(background='#DAF7A6')
        fr2 = Frame(self.root, width='250', height='150', bg='#FF9600')
        fr2.place(x=125, y=240)

        # Name Entry
        name = Label(fr2, text=":اسم المستخدم", bg='#DAF7A6', fg='black', width=11)
        name.place(x=150, y=8)
        nameplace = Entry(fr2, bg='white', fg='black', width=20, textvariable=self.inter)
        nameplace.place(x=8, y=10)

        # Password Entry
        passwo = Label(fr2, text=":كلمة المرور", bg="#DAF7A6", fg='black', width=11)
        passwo.place(x=150, y=40)
        passplace = Entry(fr2, bg="white", fg='black', width=20, textvariable=self.passinter, show='*')
        passplace.place(x=8, y=40)

        # About button
        pic0 = Image.open("c:\\Users\\Sirius\\Documents\\Visual Studio\\Project\\photo\\info.png")#================info pic=====================
        res = pic0.resize((20, 20))
        pico = ImageTk.PhotoImage(res)
        about = Button(self.root, width=20, height=20, image=pico, command=self.inabout)
        about.place(x=1, y=1)

        # Navigation in entries
        entries = [child for child in fr2.winfo_children() if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: self.next(e, entries, idx))

        # Login buttons
        signup = Button(fr2, text="Admin", bg="#27A7DB", fg='black', width=10, command=self.admin)
        signup.place(x=40, y=105)
        signtr = Button(fr2, text="Teacher", bg="silver", fg='black', width=10, command=self.Teacher)
        signtr.place(x=130, y=105)
        bt = Button(fr2, text='تسجيل الدخول', width='10', height='1', bg='#9EADAA', command=self.inapp, activebackground='silver')
        bt.place(x=130, y=70)
        bt1 = Button(fr2, text="الخروج", width='10', height='1', bg='#F52E1B', command=self.close, activebackground='silver')
        bt1.place(x=40, y=70)

        
        pic = Image.open("c:\\Users\\Sirius\\Documents\\Visual Studio\\Project\\photo\\school.png")# ==============school image=============
        res = pic.resize((250, 180))
        pic1 = ImageTk.PhotoImage(res)
        lab2 = Label(self.root, image=pic1)
        lab2.place(x=125, y=50)
        self.root.mainloop()

    def inabout(self):
        AboutUs.about()

    def func(self, event):
        self.nameplace.focus()

    def next(self, event, entry_list, this_index):
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()
        if next_index == 0:
            self.inapp()
            self.nameplace.focus()
            self.bt.bind('<Return>', self.func)

    def get_name(self):
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()
        student_name = self.inter.get()
        try:
            cur.execute("SELECT id FROM students WHERE id = %s LIMIT 1", (student_name,))
            u = cur.fetchone()
            self.name = u[0]
            print(self.name)
            lo.commit()
            lo.close()
            return str(self.name)
        except Exception as e:
            messagebox.showerror('Error', f"Database error: {e}")
            self.back()

    def get_pass(self):
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()
        id_name = self.inter.get()
        cur.execute("SELECT password FROM students WHERE id = %s LIMIT 1", (id_name,))
        u = cur.fetchone()
        self.password = u[0]
        lo.commit()
        lo.close()
        return self.password

    def back(self):
        self.root.destroy()

    def inapp(self):
        if self.inter.get() == self.get_name() and self.passinter.get() == self.get_pass():
            self.back()
            student432.Student432(self.inter.get(), self.passinter.get())
        elif self.inter.get() == "" and self.passinter.get() == "":
            self.root.update()
            messagebox.showerror("Error", 'كل الحقول فارغة!')
        else:
            messagebox.askretrycancel('رسالة ادارية', 'رقم التسلسل الذي ادخلته غير صحيح أو كلمة المرور غير مسجلة-تأكد من المدخلات أو راجع الادارة!')

    def admin(self):
        loginAdmin.LoginAdmin()

    def Teacher(self):
        loginTeacher.LoginTeacher()

    def close(self):
        no = messagebox.askokcancel("تسجيل الخروج", "هل أنت متأكد من الخروج؟")
        if no:
            self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = Main_Login(root)
    root.mainloop()
