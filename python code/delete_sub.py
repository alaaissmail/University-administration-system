from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from keyboard import press
import mysql.connector




class DELETE:
    def __init__(self):
        self.login = Toplevel()
        self.login.title("Delete Subject")
        self.login.geometry('350x140+800+100')
        self.login.resizable(False,False)
        self.login.config(backgroun='#a9b6f4')
        
        self.IDvar =StringVar()
        self.subvar =StringVar()
      
        id=Label(self.login,text="ID",bg='white',fg='black',width=20)
        id.place(x=200,y=8)
        idplace=Entry(self.login,bg='white',fg='black',width=20,textvariable=self.IDvar)
        idplace.place(x=50,y=10)

#-------------------subjectrd------------
        subject=Label(self.login,text="المادة المراد حذفها",bg="white",fg='black',width=20)
        subject.place(x=200,y=40)
        subplace=Entry(self.login,bg="white",fg='black',width=20,textvariable= self.subvar)
        subplace.place(x=50,y=40)
        bt=Button(self.login,text='حذف',width=13,height=1,bg='red',command= self.inapp,activebackground='red',fg= 'white')
        bt.place(x=190,y=70)
        back=Button( self.login ,text="الرجوع", bg="blue",fg='white', height=1 , width=13,activebackground='silver',command=self.back)
        back.place(x=70,y=70)

        def func(event):
            idplace.focus()
        def next(event, entry_list, this_index):
            next_index = (this_index + 1) % len(entry_list)
            entry_list[next_index].focus_set()
            if next_index==0:
                self.inapp()
                idplace.focus()
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
        all = {}
        id = self.IDvar.get()
        out = self.subvar.get()
    
        lo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='studentdb'
    )
    
        cur = lo.cursor()
        do0=lo.cursor()
        do1 = lo.cursor()
    # Fetch values for subjects and build the dictionary
        for i in range(1, 6):
            sub = f'subject{i}'
            query = f"SELECT {sub} FROM courses WHERE id = %s LIMIT 1"
            cur.execute(query, (id,))
            u = cur.fetchone()
            all[u[0]] = f'subject{i}'  

        if out in all.keys():
             update_query = f"UPDATE courses SET {all[out]} = 'None' WHERE id = %s"
             new = f'update subject_table set {out} = "None" where {out}=%s'
             do1.execute(new,(id,))
             do0.execute(update_query, (id,))
             self.back()
           
        lo.commit()
        lo.close()
