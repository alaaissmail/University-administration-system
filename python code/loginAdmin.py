from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from keyboard import press
import admin1


class LoginAdmin:
    def __init__(self):
        self.login = Toplevel()
        self.login.title("Admin Login")
        self.login.geometry('350x140+800+100')
        self.login.resizable(False,False)
        self.login.config(backgroun='#a9b6f4')
        
        self.inter =StringVar()
        self.passinter =StringVar()
      
        name=Label(self.login,text=":اسم المستخدم",bg='white',fg='black',width=11)
        name.place(x=200,y=8)
        nameplace=Entry(self.login,bg='white',fg='black',width=20,textvariable=self.inter)
        nameplace.place(x=50,y=10)

#-------------------password------------
        passwo=Label(self.login,text=":كلمة المرور",bg="white",fg='black',width=11)
        passwo.place(x=200,y=40)
        passplace=Entry(self.login,bg="white",fg='black',width=20,textvariable= self.passinter,show='*')
        passplace.place(x=50,y=40)
        bt=Button(self.login,text='تسجيل الدخول',width=13,height=1,bg='#0e33e5',command= self.inapp,activebackground='green',fg= 'white')
        bt.place(x=190,y=70)
        signup=Button( self.login ,text="الرجوع", bg="red",fg='white', height=1 , width=13,activebackground='red',command=self.back)
        signup.place(x=70,y=70)

        def func(event):
            nameplace.focus()
        def next(event, entry_list, this_index):
            next_index = (this_index + 1) % len(entry_list)
            entry_list[next_index].focus_set()
            if next_index==0:
                self.inapp()
                nameplace.focus()
                bt.bind('<Return>', func)

        entries = [child for child in self.login.winfo_children() if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
               entry.bind('<Return>', lambda e, idx=idx: next(e, entries, idx))

    def close(self):
           no=messagebox.askokcancel("Log Out", "are You sure you want Log out ?")
           if no == True:
               self.login.quit()
    def back(self):  #-------------------------------back Clear-----------------------------------
        self.login.destroy()
        #self.login.update()
    
#-----------------------------login app---------------------- 
    def inapp(self):
            if self.inter.get().lower() == "nuri benbarka" and self.passinter.get() == "1234":
                self.back()
                bomb = admin1.Student()
            elif self.inter.get() == "" and self.passinter.get() == "":
                messagebox.showerror("Error",'All fields are empty!')
            else :
                messagebox.askretrycancel('invailed','Sorry your name or password is not correct!')  



