from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import mysql.connector
from pathlib import Path
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import ImageTk
from pass432 import Pass
#courses 

class TEacher:
    def __init__(self,name) :
        self.stu=Toplevel() 
        self.stu.geometry("1350x695")
        self.stu.title("برنامج تسجيل الطلاب")  
        self.stu.config(background="silver")
        self.stu.resizable(False,False)
        self.Name=name

        #--------------Variable-------------
        self.seriesvar=StringVar()
        self.subvar= StringVar()
        self.numvar = StringVar()
        self.seatvar = StringVar()

        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
        cur1=lo.cursor()
        
        cur.execute("select career from teacher where name= %s LIMIT 1",(name,))
        u=cur.fetchone()
        self.subvar = u[0]     
        print(self.subvar)

        cur1.execute("select seat from teacher where name= %s LIMIT 1",(name,))
        h=cur1.fetchone()
        self.seatvar = h[0]  
                 
        cur1.execute("select id from teacher where name= %s LIMIT 1",(name,))
        d=cur1.fetchone()
        self.seriesvar = d[0]                                  

        lo.commit()
        lo.close()         


        self.idvar=StringVar()
        self.namevar=StringVar()
        self.attendvar=StringVar()
        self.midtermvar=StringVar()
        self.finalvar=StringVar()
        self.totalvar=StringVar()
        self.evaluressvar=StringVar()
        self.svar=StringVar()
        self.sby=StringVar()
        self.delevar=StringVar()
        self.final_grade=IntVar()
        self.total_grade=IntVar()

        

        #-----------program look------------
        lb1=Label(self.stu, text="منظومة تنزيل المواد",font=("monospace",14),fg="white",bg='#2045f8')
        lb1.pack(fill=X)
        fr1=Frame(self.stu,bg="white")
        fr1.place(x=1082,y=28,height=390,width=280)
        
        #---------Enter Informaton----------
        id=Label(fr1,text=" ID",fg="black",bg="white",width=30)
        id.pack()
        idtext=Label(fr1,bd='2',textvariable=self.idvar,width=30,text=self.idvar,bg='silver')
        idtext.pack()
        name=Label(fr1,text="اسم الطالب",fg="black",bg="white",width=30)
        name.pack()
        nametext=Label(fr1,bd='2',textvariable=self.namevar,width=30,text=self.namevar,bg='silver')
        nametext.pack()
        atend=Label(fr1,text="درجة الحضور",fg="black",bg="white",width=30)
        atend.pack()
        attendtext=Entry(fr1,justify="center",bd='2',textvariable=self.attendvar,width=30)
        attendtext.pack()
        mid=Label(fr1,text="درجة اعمال الفصل",fg="black",bg="white",width=30)
        mid.pack()
        midtext=Entry(fr1,justify="center",bd='2',textvariable=self.midtermvar,width=30)
        midtext.pack()
        habit=Label(fr1,text="درجة النهائي",fg="black",bg="white",width=30)
        habit.pack()
        finaltext=Entry(fr1,justify="center",bd='2',textvariable=self.finalvar,width=30)
        finaltext.pack()
        total=Label(fr1,text="الدرجة الكلية",fg="black",bg="white",bd='2')
        total.pack()
        totaltext=Label(fr1,textvariable=self.totalvar,bd='2',width=30,justify="center",bg='silver')
        totaltext.pack()
        evalu=Label(fr1,text="التقدير",fg="black",bg="white")
        evalu.pack()
        evalutext=Label(fr1,justify="center",bd='2',textvariable=self.evaluressvar,width=30,bg='silver')
        evalutext.pack()


        #---------------buttons--------------
        btfr=Frame(self.stu,bg="white")
        btfr.place(x=1082,y=420,height=276,width=280)
        title=Label(btfr,text="التحكم",font=("Deco",14),bg="#2045f8",fg="white")
        title.pack(fill=X)

        evalustudent=Button(btfr,text="ادراج الدرجات ",bg="silver",activebackground="#04A70E",command=self.add_score)
        evalustudent.place(x=40,y=33,width='200',height='40')
        remo=Button(btfr,text="تعديل المعلومات", bg="silver",activebackground="#FA0202",command=self.update)
        remo.place(x=40,y=73,width='200',height='40')
        edit=Button(btfr,text="حساب التقدير",bg="silver",activebackground="#2980B9", command= self.eva)
        edit.place(x=40,y=113,width='200',height='40')
        dele=Button(btfr,text="اعادة تعيين كلمة المرور",bg="silver",activebackground="pink",command=self.new_pass)
        dele.place(x=40,y=153,width='200',height='40')
        who=Button(btfr,text="About Us",bg="silver",activebackground="pink",command=self.abt)
        who.place(x=40,y=193,width='200',height='40')
        Exit=Button(btfr,text="Exit",bg="silver",activebackground="black",activeforeground="white",command=quit)
        Exit.place(x=40,y=233,width='200',height='40')

        #--------------search manage-------------
        sfr=Frame(self.stu,bg="white")
        sfr.place(x=3,y=28,width=1077,height=40)
        slb=Label(sfr,text="Search For a Student:",font=10,fg="Black",bg="white")
        slb.place(x=18,y=9)
        scombo=ttk.Combobox(sfr,textvariable= self.sby)
        scombo['values']=('ID')#-----arranged-----

        #----------------------------refresh----------------------------
        self.pic=Image.open("c:\\Users\\Sirius\\Documents\\Visual Studio\\Project\\photo\\refresh.png")#====================refresh pic==============
        self.res=self.pic.resize((20,20)) 
        self.pico=ImageTk.PhotoImage(self.res)
        
        review=Button(sfr ,height=22, width=20, image= self.pico,command=self.refresh)
        review.place(x=1042,y=4)  

        scombo.place(x=200,y=9)
        sentry=Entry(sfr,bd='2',textvariable=self.svar,width=23)
        sentry.place(x=365,y=7)
        sbt=Button(sfr,text="بحث",fg="black",bg="silver",height=1,width=25,activebackground="#3498DB",command=self.search)
        sbt.place(x=530,y=4)
        lb10=Label(sfr,text= str(self.seatvar) + ": عدد المقاعد ",fg="black",bg="silver",height=2,width=13,activebackground="#3498DB",font='bond')
        lb10.place(x=750,y=4)
        lb20=Label(sfr,text=str(self.subvar) +":المادة" ,fg="black",height=2,width=15,activebackground="#3498DB",bg='silver',font='bond')
        lb20.place(x=880,y=4)        
       
        #------------show Information-------------
        showfr=Frame(self.stu,bg='pink')
        showfr.place(x=3,y=72,width=1076,height=622)
        
        ycrol=Scrollbar(showfr,orient=VERTICAL)
        ycrol.pack(side="right",fill=Y)
        xcrol=Scrollbar(showfr,orient=HORIZONTAL)
        xcrol.pack(side="bottom",fill=X)
        
        #----------------Treeview-----------------
        #-------------arranged columns----------
        self.student=ttk.Treeview(showfr,columns=('idtext','nametext','attendtext','midtext','finaltext','totaltext','evaluresstext'),xscrollcommand=xcrol.set,yscrollcommand=ycrol.set)
        self.student.place(x=1,y=1,width=1064,height=605)
        xcrol.config(command=self.student.xview)
        ycrol.config(command=self.student.yview)

        #---------Treeview Heads (student table)----------
        self.student['show']='headings',
        self.student.heading("idtext",text=" ID")
        self.student.heading("nametext",text="اسم الطالب")
        self.student.heading("attendtext",text="درجة الحضور")
        self.student.heading("midtext",text="درجة اعمال الفصل")
        self.student.heading("finaltext",text="درجة النهائي")
        self.student.heading("totaltext",text="الدرجة الكلية")
        self.student.heading("evaluresstext",text="التقدير")

        #----------Treeview size-------------
        self.student.column('idtext',width=17)
        self.student.column('nametext',width=100)
        self.student.column('attendtext',width=100)
        self.student.column('midtext',width=50)
        self.student.column('finaltext',width=65)
        self.student.column('totaltext',width=15)
        self.student.column('evaluresstext',width=120)
        self.student.bind('<ButtonRelease-1>',self.mycursor)#-------evalu informatiom to fields--------
        self.comeback()
        
        #---------connection with database + evalu------------
        self.comeback()

    def num(self):
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
       
        cur2=lo.cursor()        
        cur2.execute("select num from students where id= %s LIMIT 1",(self.idvar.get(),))
        k=cur2.fetchone()
        try:
            self.numvar = k[0]
        except:
           return 0
        lo.commit()
        lo.close()
        return self.numvar
        
    def new_pass(self):
        p = Pass(self.seriesvar)    
    
    def total1(self):
         sum = 0
         sum=sum+int(self.attendvar.get())+int(self.midtermvar.get())+int(self.finalvar.get())
         if sum > 100 : 
            messagebox.askretrycancel("Error" , "! الرجاء التأكد من درجات الطالب المدخلة ")            
         return sum
    
    def add_score(self):
        evaluation = self.evaluressvar.get()

        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )

        cur=lo.cursor()
      
        try:
           num1 = self.num()
           cur.execute('update  score_table set attend=%s,midterm=%s,final=%s,total=%s,evaluation=%s where sub = %s and num =%s',(self.attendvar.get(),
          self.midtermvar.get(),
          self.finalvar.get(),
          self.totalvar.get(),
          evaluation,
          self.subvar,
          num1,
          ))
        except: 
             messagebox.askretrycancel("Error" , "الرجاء اتباع التعليمات")
        lo.commit()
        self.comeback()#------show before Exit -------
        lo.close()

    
    #---------to show Data----------
    def comeback(self):
        come=mysql.connector.connect(host='localhost',user='root',password='#User#Root:#123',database='StudentDB')
        do=come.cursor()
        do.execute('select id , name , attend , midterm , final , total , evaluation from score_table where sub = %s ', (self.subvar,))
        rows= do.fetchall()#-----bring all data-----
        if len(rows)!=0:
            self.student.delete(*self.student.get_children())
            for row in rows:#---------loop for bring it up to the table-------
                self.student.insert('',END,values=row)
            come.commit()
        come.close()

    #----------delet fields------
    def clear(self):
             self.idvar.set('')
             self.namevar.set('')
             self.attendvar.set('')
             self.midtermvar.set('')
             self.finalvar.set('')
             self.totalvar.set('')
             self.evaluressvar.set('')
  
    def calculate_final_grade(self):

        try:
         if self.attendvar.get()!="None" and self.midtermvar.get()!="None" and self.finalvar.get()!="None":

           self.final_grade = int(self.attendvar.get()) + int(self.midtermvar.get()) + int(self.finalvar.get())

           if 85 <= self.final_grade <= 100:
              self.evaluressvar = 'ممتاز'
           elif 75 <= self.final_grade <= 84:
               self.evaluressvar = 'جيد جدا'
           elif 60 <= self.final_grade <= 74:
               self.evaluressvar = "جيد"
           elif 50 <= self.final_grade <= 59:
               self.evaluressvar = 'مقبول'
           elif  self.final_grade < 50:
               self.evaluressvar = 'ضعيف'
           else:
             messagebox.showerror("Error","الرجاء التأكد من الدرجات المدخلة")             
                        
               
           return self.evaluressvar    
        except:
             messagebox.showerror("Error","الرجاء التأكد من الدرجات المدخلة")             
    
    def calculate_total_grade(self):
     
        if self.attendvar.get()!="None" and self.midtermvar.get()!="None" and self.finalvar.get()!="None":

           self.total_grade = int(self.attendvar.get()) + int(self.midtermvar.get()) + int(self.finalvar.get())
        return str(self.total_grade)             

    def update(self):
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )

        cur=lo.cursor()
      
        #try:
        num1 = self.num()
        cur.execute('update  score_table set attend=%s,midterm=%s,final=%s,total=%s,evaluation=%s where sub = %s and num =%s',(self.attendvar.get(),
          self.midtermvar.get(),
          self.finalvar.get(),
          self.totalvar.get(),
          self.evaluressvar,
          self.subvar,
          num1,
          ))
        #except: 
            #messagebox.askretrycancel("Error" , "الرجاء تحديد الطالب المراد ادراج درجاته")
        lo.commit()
        self.comeback()#------show before Exit -------
        lo.close()

    def eva(self):
        num = self.num()
        out = self.calculate_final_grade()

        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb')
        cur=lo.cursor()

        c = 'update  score_table set evaluation = %s where num = %s and sub =%s'
        cur.execute(c,(out,num,self.subvar))

        lo.commit()
        self.total()
        self.comeback()
        self.clear()
        lo.close() 

    def total(self):
        out = self.calculate_total_grade()
        num = self.num()
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb')
        cur=lo.cursor()

        c = 'update  score_table set total = %s where num = %s and sub =%s'
        cur.execute(c,(out,num,self.subvar))

        lo.commit()
        self.comeback()
        lo.close()         

    def mycursor(self,ev):#ev is your event that have everything 
         info=self.student.focus()
         contents=self.student.item(info)
         row=contents['values']
         self.idvar.set(row[0])
         self.namevar.set(row[1])
         self.attendvar.set(row[2])
         self.midtermvar.set(row[3])
         self.finalvar.set(row[4])
         self.totalvar.set(row[5])
         self.evaluressvar.set(row[6])
         

    def clear(self):
         
         self.idvar.set("")
         self.namevar.set(""),
         self.attendvar.set(""),
         self.midtermvar.set(""),
         self.finalvar.set(""),
         self.totalvar.set(""),
         self.evaluressvar='' 
         
    #---------------update-----------

    #----------------search def--------------              


    def search(self):
    # ============================Establish connection======================================
     con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='StudentDB'
    )
    
     try:
        do = con.cursor()    
        query = "SELECT id , name , attend , midterm , final , total , evaluation FROM score_table WHERE id LIKE %s AND sub LIKE %s"       
        do.execute(query, ('%' + self.idvar.get() + '%', '%' + self.subvar+ '%'))       
        rows = do.fetchall()

        if len(rows) != 0:
            self.student.delete(*self.student.get_children())       
        for row in rows:
            self.student.insert('', END, values=row)
    
     except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    
     except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    
     finally:
        if con.is_connected():
            con.close()
        con.commit()
        con.close()

    def refresh(self):
        try:
           self.comeback()
           self.clear()
        except:
            messagebox.askretrycancel('Error','الرجاء اتباع التعليمات !')           
    
    #-----------------about us--------------    
    def abt(self):
            messagebox.showinfo("About US!", 'we are a team of university student developers. \n Thanks For Your Supports')
