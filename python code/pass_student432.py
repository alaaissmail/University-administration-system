from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from keyboard import press
import mysql.connector


class Pass:
    def __init__(self,id):
        self.login = Toplevel()
        self.login.title("PassWord")
        self.login.geometry('350x140+800+100')
        self.login.resizable(False,False)
        self.login.config(backgroun='#a9b6f4')
        
        self.currentvar =StringVar()
        self.newevar =StringVar()
        self.id= id
      
        current=Label(self.login,text="كلمة المرور الحالية",bg='white',fg='black',width=20)
        current.place(x=190,y=8)
        curplace=Entry(self.login,bg='white',fg='black',width=20,textvariable=self.currentvar,show='*')
        curplace.place(x=50,y=10)

#-------------------subjectrd------------
        new=Label(self.login,text="كلمة المرور الجديدة" ,bg="white",fg='black',width=20)
        new.place(x=190,y=40)
        newplace=Entry(self.login,bg="white",fg='black',width=20,textvariable= self.newevar,show='*')
        newplace.place(x=50,y=40)
        bt=Button(self.login,text='موافق',width=13,height=1,bg='green',command= self.inapp,activebackground='red',fg= 'white')
        bt.place(x=190,y=70)
        back=Button( self.login ,text="الرجوع", bg="blue",fg='white', height=1 , width=13,activebackground='silver',command=self.back)
        back.place(x=70,y=70)

        def func(event):
            curplace.focus()
        def next(event, entry_list, this_index):
            next_index = (this_index + 1) % len(entry_list)
            entry_list[next_index].focus_set()
            if next_index==0:
                self.inapp()
                curplace.focus()
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
    
#-----------------------------login app---------------------- 
    def inapp(self):
        current = self.currentvar.get()
        new = self.newevar.get()
    
        lo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='studentdb'
    )
    
        cur = lo.cursor()
        do1 = lo.cursor()

        query = f"SELECT password FROM students WHERE id = %s LIMIT 1"
        cur.execute(query, (self.id,))
        u = cur.fetchone()
        old = u[0]
        
        if str(old) == str(current) :
             b = "UPDATE students SET password = %s WHERE id = %s"
             do1.execute(b,(new,self.id))
             messagebox.askokcancel("ِAlert", "تم تعيين كلمة المرور الجديدة")    
             self.back()
        elif current == '' and new == '':
                messagebox.showerror("Error",' كل الحقول فارغة ')                  
        else:
             messagebox.askretrycancel("Error", " كلمة المرور الحالية غير صحيحة! \nالرجاء اعادة المحاولة")    
           
        lo.commit()
        lo.close()
