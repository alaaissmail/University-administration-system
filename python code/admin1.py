from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
from PIL import ImageTk
from addCourse import inserted_courses
import addCourse
import delete_sub

class Student:
    def __init__(self) :
        self.stu= Toplevel()
        self.stu.geometry("1350x695")
        self.stu.title("برنامج تسجيل الطلاب")  
        self.stu.config(background="silver")
        self.stu.resizable(False,False)
 
        #--------------Variable-------------
        self.idvar=StringVar()
        self.namevar=StringVar()
        self.datevar=StringVar()
        self.phonevar=StringVar()
        self.nationvar=StringVar()
        self.gendervar=StringVar()
        self.addressvar=StringVar()
        self.cityvar=StringVar()
        self.watanivar=StringVar()
        self.svar=StringVar()
        self.sby=StringVar()
        self.delevar=StringVar()

        #------------------------courses------------------
        self.sub1var=StringVar()
        self.sub2var=StringVar()
        self.sub3var=StringVar()
        self.sub4var=StringVar()
        self.sub5var=StringVar()
        self.sub6var=StringVar()
        self.scorevar=StringVar()
        self.semvar=StringVar()
        self.semvar=StringVar()
        self.btfr = None
        self.numvar=StringVar()

        #====================teacher data==============
        self.seriesvar=StringVar()
        self.teachervar=StringVar()
        self.teacherSubject=StringVar()#----------------------------المؤهل العلمي-----------------------
        self.teachergrad=StringVar()
        self.qualivar=StringVar()
        self.careervar=StringVar()
        self.wahdavar=StringVar()
        self.seatsvar=StringVar()
        #==============================hash======================

        delete1= self.idvar.get()
        #def info():
            #messagebox.askokcancel("Information",'Sorry Sir, there something wrong!')

        #-----------program look------------
        lb1=Label(self.stu, text="منظومة تنزيل المواد",font=("monospace",14),fg="white",bg='#2045f8')
        lb1.pack(fill=X)
        
        #===========================search=============================
        sfr=Frame(self.stu,bg="white")
        sfr.place(x=3,y=28,width=1077,height=40)
        slb=Label(sfr,text="Search For a Student:",font=10,fg="Black",bg="white")
        slb.place(x=3,y=4)
        scombo=ttk.Combobox(sfr,textvariable= self.sby)
        scombo['values']=('ID','name','nation','gender')#-----arranged-----
        scombo.place(x=175,y=5)
        sentry=Entry(sfr,bd='2',textvariable=self.svar,width=23)
        sentry.place(x=325,y=5)
        sbt=Button(sfr,text="بحث",fg="black",bg="silver",height=1,width=10,activebackground="#3498DB",command=self.search)
        sbt.place(x=480,y=5)

        #---------------------------------important student info------------
        stdinfo=Button(sfr,text="معلومات الطلاب",fg="black",bg="silver",height=1,width=21,activebackground="#3498DB",command=self.infoStudent)
        stdinfo.place(x=564,y=4)

        stdcur=Button(sfr,text="مواد الطلاب",fg="black",bg="silver",height=1,width=21,activebackground="#3498DB",command= self.curces)
        stdcur.place(x=723,y=4)

        teacher=Button(sfr,text="معلومات المعلمين",fg="black",bg="silver",height=1,width=21,activebackground="#3498DB",command=self.Teacher)
        teacher.place(x=882,y=4)        
        #--------------------------refreshButtom------------------------------
        #----------------------------refresh----------------------------
        self.pic=Image.open("c:\\Users\\Sirius\\Documents\\Visual Studio\\Project\\photo\\refresh.png")#======================refresh pic==================
        self.res=self.pic.resize((20,20)) 
        self.pico=ImageTk.PhotoImage(self.res)
        
        review=Button(sfr ,height=22, width=20, image= self.pico,command=self.refresh)
        review.place(x=1042,y=4)  

    def student_data(self):
        fr1=Frame(self.stu,bg="white")
        fr1.place(x=1082,y=28,height=390,width=280)
        #---------Enter Informaton----------
        id=Label(fr1,text="رقم قيد الطالب",fg="black",bg="white")
        id.pack()
        idtext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.idvar)
        idtext.pack()
        name=Label(fr1,text="اسم الطالب الرباعي",fg="black",bg="white",width=30)
        name.pack()
        nametext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.namevar)
        nametext.pack()
        date=Label(fr1,text="تاريخ الميلاد",width=30,fg="black",bg="white")
        date.pack()
        datetext= DateEntry(fr1, selectmode = 'year', year = 2000 , month = 1, day = 1 , date_pattern = 'dd/mm/yyyy' , textvariable=self.datevar)
        datetext.pack()
        nation=Label(fr1,text="الجنسية",fg="black",bg="white")
        nation.pack()
        nationtext=Entry(fr1,justify="left",width=30,bd='2', textvariable= self.nationvar)
        nationtext.pack()
        watania=Label(fr1,text=" الرقم الوطني",fg="black",width=30,bg="white")
        watania.pack()
        watanitext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.watanivar)
        watanitext.pack()
        check=Label(fr1,text="الجنس",width=30,fg="black",bg="white")
        check.pack()
        checktext=ttk.Combobox(fr1,values="ذكر أنثى", state ="readonly",textvariable=self.gendervar)
        checktext.pack()
        phone=Label(fr1,text="رقم الهاتف",width=30,fg="black",bg="white")
        phone.pack()
        phonetext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.phonevar)
        phonetext.pack()
        city=Label(fr1,text="المدينة",width=30,fg="black",bg="white")
        city.pack()
        citytext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.cityvar)
        citytext.pack()
        address=Label(fr1,text="عنوان السكن",width=30,fg="black",bg="white")
        address.pack()
        addresstext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.addressvar)
        addresstext.pack()
        
        def next(event, entry_list, this_index):
            next_index = (this_index + 1) % len(entry_list)
            entry_list[next_index].focus_set()
            if next_index==0:
                 self.add_student()
                 self.clear()
                 

        entries = [child for child in fr1.winfo_children() if isinstance(child, Entry)]

        for idx, entry in enumerate(entries):
           entry.bind('<Return>', lambda e, idx=idx: next(e, entries, idx))
#refresh
        #---------------buttons--------------
        self.btfr=Frame(self.stu,bg="white")
        self.btfr.place(x=1082,y=420,height=276,width=280)
        title=Label(self.btfr,text="التحكم",font=("Deco",14),bg="#2045f8",fg="white")
        title.pack(fill=X)
        
        addstudent=Button(self.btfr,text="اضافة طالب",bg="silver",activebackground="#04A70E",command=self.add_student)
        addstudent.place(x=40,y=33,width='200',height='40')
        remo=Button(self.btfr,text="اعادة تعيين كلمة المرور",bg="silver",activebackground="#2980B9",command=self.Pass_student)
        remo.place(x=40,y=73,width='200',height='40')
        edit=Button(self.btfr,text="تعديل معلومات",bg="silver",activebackground="pink", command= self.update)
        edit.place(x=40,y=113,width='200',height='40')
        dele=Button(self.btfr,text="حذف طالب",bg="silver",activebackground="red",command= self.delete)
        dele.place(x=40,y=153,width='200',height='40')
        who=Button(self.btfr,text="حذف الحقول",bg="silver",activebackground="pink",command=self.clear)
        who.place(x=40,y=193,width='200',height='40')
        Exit=Button(self.btfr,text="Exit",bg="silver",activebackground="black",activeforeground="white",command=self.back)
        Exit.place(x=40,y=233,width='200',height='40')
        #==================curse panel=====================

    def infoStudent(self):
        #------------show Information-------------
            showfr=Frame(self.stu,bg='pink')
            showfr.place(x=3,y=72,width=1076,height=622)
        #-------------arranged columns----------

            ycrol=Scrollbar(showfr,orient=VERTICAL)
            ycrol.pack(side="right",fill=Y)
            xcrol=Scrollbar(showfr,orient=HORIZONTAL)
            xcrol.pack(side="bottom",fill=X)     
        #----------------Treeview-----------------           
            self.student=ttk.Treeview(showfr,columns=('idtext','nametext','datetext','nationtext','watanitext','checktext','phonetext','citytext','addresstext'),xscrollcommand=xcrol.set,yscrollcommand=ycrol.set)
            self.student.place(x=1,y=1,width=1064,height=605)
            xcrol.config(command=self.student.xview)
            ycrol.config(command=self.student.yview)

        #---------Treeview Heads (student table)----------
            self.student['show']='headings',
            self.student.heading("idtext",text="رقم القيد")        
            self.student.heading("addresstext",text="عنوان السكن")
            self.student.heading("citytext",text="المدينة")
            self.student.heading("phonetext",text="رقم الهاتف")      
            self.student.heading("checktext",text="الجنس")
            self.student.heading("watanitext",text="الرقم الوطني")
            self.student.heading("nationtext",text="الجنسية")
            self.student.heading("datetext",text="تاريخ الميلاد")
            self.student.heading("nametext",text="اسم الطالب")

        #----------Treeview size-------------
            self.student.column('idtext',width=50)
            self.student.column('addresstext',width=30)
            self.student.column('citytext',width=30)
            self.student.column('phonetext',width=50)
            self.student.column('checktext',width=30)
            self.student.column('watanitext',width=70)
            self.student.column('nationtext',width=40)
            self.student.column('datetext',width=45)
            self.student.column('nametext',width=50)
        
            self.student.bind('<ButtonRelease-1>',self.mycursor)#-------add informatiom to fields--------(<event>+function)
            self.comeback()
            self.student_data()
        
        #---------connection with database + add------------
            self.comeback()

    def curces(self):
            self.clear_sub()
            #---------------------------text -----------------------------
            fr1=Frame(self.stu,bg="white")
            fr1.place(x=1082,y=28,height=450,width=280)    
            id=Label(fr1,text="رقم قيد الطالب",fg="black",bg="white")
            id.pack()
            idtext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.idvar)
            idtext.pack()
            name=Label(fr1,text="اسم الطالب الرباعي",fg="black",bg="white",width=30)
            name.pack()
            nametext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.namevar)
            nametext.pack()
            sub1=Label(fr1,text="Subject1",width=30,fg="black",bg="white")
            sub1.pack()
            sub1text= Entry(fr1,justify='left' , width=30, fg= 'black', textvariable=self.sub1var)
            sub1text.pack()
            sub2=Label(fr1,text="Subject2",fg="black",bg="white")
            sub2.pack()
            sub2text=Entry(fr1,justify="left",width=30,bd='2', textvariable= self.sub2var)
            sub2text.pack()
            sub3=Label(fr1,text="Subject3",fg="black",width=30,bg="white")
            sub3.pack()
            sub3text=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.sub3var)
            sub3text.pack()
            sub4=Label(fr1,text="Subject4",width=30,fg="black",bg="white")
            sub4.pack()
            sub4text=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.sub4var)
            sub4text.pack()
            sub5=Label(fr1,text="Subject5",width=30,fg="black",bg="white")
            sub5.pack()
            sub5text=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.sub5var)
            sub5text.pack()
            sub6=Label(fr1,text="Subject6",width=30,fg="black",bg="white")
            sub6.pack()
            sub6text=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.sub6var)
            sub6text.pack()
            score=Label(fr1,text="المعدل",width=30,fg="black",bg="white")
            score.pack()
            scoretext=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.scorevar)
            scoretext.pack()
            sem=Label(fr1,text="الفصل الدراسي",width=30,fg="black",bg="white")
            sem.pack()
            semtext=Entry(fr1,justify="left",bd='2',width=30,textvariable=self.semvar)
            semtext.pack()
        #------------show Information-------------
            showfr=Frame(self.stu,bg='pink')
            showfr.place(x=3,y=72,width=1076,height=622)
        #-------------arranged columns----------

            ycrol=Scrollbar(showfr,orient=VERTICAL)
            ycrol.pack(side="right",fill=Y)
            xcrol=Scrollbar(showfr,orient=HORIZONTAL)
            xcrol.pack(side="bottom",fill=X)     

            def next(event, entry_list, this_index):
                next_index = (this_index + 1) % len(entry_list)
                entry_list[next_index].focus_set()
                if next_index==0:
                    self.add_subject()
                    self.clear()
                 

            entries = [child for child in fr1.winfo_children() if isinstance(child, Entry)]

            for idx, entry in enumerate(entries):
                 entry.bind('<Return>', lambda e, idx=idx: next(e, entries, idx))      
            
            
        #-------------------------Treeview-----------------           
            self.curse=ttk.Treeview(showfr,columns=('idtext','nametext','sub1text','sub2text','sub3text','sub4text','sub5text','sub6text',"who","scoretext",'semtext'),xscrollcommand=xcrol.set,yscrollcommand=ycrol.set)
            self.curse.place(x=1,y=1,width=1064,height=605)
            xcrol.config(command=self.curse.xview)
            ycrol.config(command=self.curse.yview)

        
        #---------------------Treeview Heads (student table)----------
            self.curse['show']='headings',
            self.curse.heading("scoretext",text="% المعدل العام")
            self.curse.heading("who",text="عدد الوحدات")
            self.curse.heading("semtext",text="السيم")  
            self.curse.heading("sub6text",text="المادة 6")
            self.curse.heading("sub5text",text="المادة 5")      
            self.curse.heading("sub4text",text="المادة 4")
            self.curse.heading("sub3text",text="المادة 3")
            self.curse.heading("sub2text",text="المادة 2")
            self.curse.heading("sub1text",text="المادة 1")
            self.curse.heading("nametext",text="اسم الطالب")
            self.curse.heading("idtext",text="رقم القيد")        


        #--------------------------Treeview size----------------------

            self.curse.column('scoretext',width=30)
            self.curse.column("who",width = 30)
            self.curse.column('semtext',width=30)
            self.curse.column('sub6text',width=35)
            self.curse.column('sub5text',width=35)
            self.curse.column('sub4text',width=35)
            self.curse.column('sub3text',width=35)
            self.curse.column('sub2text',width=35)
            self.curse.column('sub1text',width=35)            
            self.curse.column('nametext',width=100)
            self.curse.column('idtext',width=50)
        
            self.curse.bind('<ButtonRelease-1>',self.mycursor_sub)#-------------------add informatiom to fields----------------(<event>+function)
            self.comeback_sub()

            self.btfr=Frame(self.stu,bg="white")
            self.btfr.place(x=1082,y=475,height=220,width=280)
            title=Label(self.btfr,text="التحكم",font=("Deco",14),bg="#2045f8",fg="white")
            title.pack(fill=X)
            addstudent=Button(self.btfr,text="اضافة مادة",bg="silver",activebackground="#04A70E",command=self.add_subject)
            addstudent.place(x=40,y=33,width='200',height='37')
            remo=Button(self.btfr,text="حذف مادة",bg="silver",activebackground="#2980B9",command=self.delete_subject)
            remo.place(x=40,y=70,width='200',height='37')
            edit=Button(self.btfr,text=" تعديل معلومات ",bg="silver",activebackground="pink", command= self.update_sub)
            edit.place(x=40,y=107,width='200',height='37')
            who=Button(self.btfr,text="حساب الوحدات",bg="silver",activebackground="pink",command=self.wahadat)
            who.place(x=40,y=144,width='200',height='37')           

        #---------connection with database + add------------
            self.comeback_sub()                  

    def wahadat(self):
      try:
        sum = 0
        all = []
        hash = {}
        for i in range(55):
            hash[inserted_courses[i][0]]=inserted_courses[i][1]

        id = self.idvar.get()
        k=0
        lo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='studentdb'
        )
    
        cur = lo.cursor()
        do0=lo.cursor()
        add=lo.cursor()
        num=lo.cursor()
        sub=lo.cursor()
        do1=lo.cursor()
        do2=lo.cursor()

        num.execute('select num from students where id=%s limit 1',(id,))
        h = num.fetchone()

    #--------------------Student Subject------------------------
        for i in range(1,7):
            sub = f'subject{i}'
            query = f"SELECT {sub} FROM courses WHERE id = %s LIMIT 1"
            cur.execute(query, (id,))
            u = cur.fetchone()
            all.append(u[0])
        
        lolo = str(h[0])    #======================add in course===============next  
        print(all)
        while k < 6 :
            if all[k] in hash.keys() and all[k] != 'None':
                sum+=hash[all[k]]
            else:
                break   
            k+=1
            
        if sum <= 18:
            do0.execute('update courses set score=%s where id='+ self.idvar.get(),(sum,))

        do1.execute('delete from score_table where num=%s', (str(lolo),))

        for i in range(6):
           if all[i] != 'None' :  
             c=f'update  subject_table set {all[i]} = %s  where num = '
             add.execute(c + lolo , ([self.idvar.get()]))
              
             t='insert into score_table (num , sub , id , name ) values (%s,%s,%s,%s) '
             do2.execute(t, (lolo , all[i],self.idvar.get(),self.namevar.get()))  

        lo.commit()
        self.comeback_sub()        
        lo.close()
  
      except:
            messagebox.askretrycancel('Error','الرجاء التأكد من القيم المدخلة و اعادة المحاولة !')   

    def Teacher(self):
            fr1=Frame(self.stu,bg="white")
            fr1.place(x=1082,y=28,height=475,width=280)
  
        #--------==========================-Teacher Informaton========================---------
            id=Label(fr1,text="رقم التسلسل",fg="black",bg="white")
            id.pack()
            seriestext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.seriesvar)
            seriestext.pack()
            name=Label(fr1,text="اسم المعلم الرباعي",fg="black",bg="white",width=30)
            name.pack()
            teachertext=Entry(fr1,justify="right",width=30,bd='2',textvariable=self.teachervar)
            teachertext.pack()
            date=Label(fr1,text="تاريخ الميلاد",width=30,fg="black",bg="white")
            date.pack()
            datetext= DateEntry(fr1, selectmode = 'year', year = 1960 , month = 1, day = 1 , date_pattern = 'dd/mm/yyyy' , textvariable=self.datevar)
            datetext.pack()
            nation=Label(fr1,text="الجنسية",fg="black",bg="white")
            nation.pack()
            nationtext=Entry(fr1,justify="left",width=30,bd='2', textvariable= self.nationvar)
            nationtext.pack()
            grad=Label(fr1,text="المؤهل العلمي",fg="black",width=30,bg="white")
            grad.pack()
            qualitext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.qualivar)
            qualitext.pack()
            check=Label(fr1,text="الجنس",width=30,fg="black",bg="white")
            check.pack()
            checktext=ttk.Combobox(fr1,values="ذكر أنثى", state ="readonly",textvariable=self.gendervar)
            checktext.pack()
            phone=Label(fr1,text="رقم الهاتف",width=30,fg="black",bg="white")
            phone.pack()
            phonetext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.phonevar)
            phonetext.pack()
            city=Label(fr1,text="المدينة",width=30,fg="black",bg="white")
            city.pack()
            citytext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.cityvar)
            citytext.pack()
            address=Label(fr1,text="عنوان السكن",width=30,fg="black",bg="white")
            address.pack()
            addresstext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.addressvar)
            addresstext.pack()
            Subject0=Label(fr1,text="المقرر العلمي",width=30,fg="black",bg="white")
            Subject0.pack()
            Subject0text=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.careervar)
            Subject0text.pack()        
            Sem0=Label(fr1,text="عدد المقاعد",width=30,fg="black",bg="white")
            Sem0.pack()
            Semtext=Entry(fr1,justify="right",bd='2',width=30,textvariable=self.seatsvar)
            Semtext.pack()            
        #--------------------to use Enter key----------------------
            def next(event, entry_list, this_index):
                next_index = (this_index + 1) % len(entry_list)
                entry_list[next_index].focus_set()
                if next_index==0:
                    self.add_student()
                    self.clear()
                 

            entries = [child for child in fr1.winfo_children() if isinstance(child, Entry)]

            for idx, entry in enumerate(entries):
              entry.bind('<Return>', lambda e, idx=idx: next(e, entries, idx))
                        
        #------------show Information-------------  
            showfr=Frame(self.stu,bg='pink')
            showfr.place(x=3,y=72,width=1076,height=622)
        #-------------arranged columns----------

            ycrol=Scrollbar(showfr,orient=VERTICAL)
            ycrol.pack(side="right",fill=Y)
            xcrol=Scrollbar(showfr,orient=HORIZONTAL)
            xcrol.pack(side="bottom",fill=X)     
        #----------------Treeview-----------------           
            self.teacher=ttk.Treeview(showfr,columns=('seriestext','teachertext','datetext','nationtext','qualitext','checktext','phonetext','citytext','addresstext','Subject0text','Semtext'),xscrollcommand=xcrol.set,yscrollcommand=ycrol.set)
            self.teacher.place(x=1,y=1,width=1064,height=605)
            xcrol.config(command=self.teacher.xview)
            ycrol.config(command=self.teacher.yview)

        #---------Treeview Heads (student table)----------
            self.teacher['show']='headings',
            self.teacher.heading("Semtext",text="عدد المقاعد")       
            self.teacher.heading("Subject0text",text="المقرر العلمي")        
            self.teacher.heading("addresstext",text="عنوان السكن")
            self.teacher.heading("citytext",text="المدينة")
            self.teacher.heading("phonetext",text="رقم الهاتف")      
            self.teacher.heading("checktext",text="الجنس")
            self.teacher.heading("qualitext",text="المؤهل العلمي")
            self.teacher.heading("nationtext",text="الجنسية")
            self.teacher.heading("datetext",text="تاريخ الميلاد")
            self.teacher.heading("teachertext",text="اسم المعلم")
            self.teacher.heading("seriestext",text="رقم التسلسل")        

        #----------Treeview size-------------
            self.teacher.column('Semtext',width=30)
            self.teacher.column('Subject0text',width=30)
            self.teacher.column('addresstext',width=30)
            self.teacher.column('citytext',width=30)
            self.teacher.column('phonetext',width=30)
            self.teacher.column('checktext',width=30)
            self.teacher.column('qualitext',width=30)
            self.teacher.column('nationtext',width=30)
            self.teacher.column('datetext',width=30)
            self.teacher.column('teachertext',width=100)
            self.teacher.column('seriestext',width=20)

        
            self.teacher.bind('<ButtonRelease-1>',self.mycursor_teacher)#-------add informatiom to fields--------(<event>+function)
            self.comeback_teacher()
            
        #------------------------Teacher Panel--------------------
            self.btfr=Frame(self.stu,bg="white")
            self.btfr.place(x=1082,y=500,height=193,width=280)
            title=Label(self.btfr,text="التحكم",font=("Deco",14),bg="#2045f8",fg="white")
            title.pack(fill=X)
            addstudent=Button(self.btfr,text="اضافة معلم",bg="silver",activebackground="#04A70E",command=self.add_teacher)
            addstudent.place(x=40,y=33,width='200',height='37')
            remo=Button(self.btfr,text="حذف معلم",bg="silver",activebackground="#2980B9",command=self.delete_teacher)
            remo.place(x=40,y=70,width='200',height='37')
            edit=Button(self.btfr,text="تعديل معلم",bg="silver",activebackground="pink",command=self.update_teacher)
            edit.place(x=40,y=107,width='200',height='37')
            who=Button(self.btfr,text="اعادة تعيين كلمة المرور",bg="silver",activebackground="pink",command=self.Pass_teacher)
            who.place(x=40,y=144,width='200',height='37')

        
        #---------connection with database + add------------
            self.comeback_teacher()
              
    def add_student (self):
        #-------ad var to connect by pymysql------
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
        new=lo.cursor()
        try:
          cur.execute('insert into students (id,name,date,nation,watani,gender,phone,city,address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.idvar.get(),
          self.namevar.get(),
          self.datevar.get(),
          self.nationvar.get(),
          self.watanivar.get(),
          self.gendervar.get(),
          self.phonevar.get(),
          self.cityvar.get(),
          self.addressvar.get()
          ))
          new.execute('insert into courses (id,name) values (%s,%s)',(self.idvar.get(),self.namevar.get()))
        except: 
            messagebox.askretrycancel("Error" , "رقم قيد الطالب موجود !")
        
        lo.commit()
        self.comeback()#------show before Exit -------
        lo.close()

    def add_subject(self):
                 #-------ad var to connect by pymysql------
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
      
        try:
           cur.execute('update courses set name=%s ,subject1=%s,subject2=%s,subject3=%s,subject4=%s ,subject5=%s,subject6=%s, pecent=%s,coursescol=%s where ID=' + self.idvar.get() ,(
           self.namevar.get(),
           self.sub1var.get(),
           self.sub2var.get(),
           self.sub3var.get(),
           self.sub4var.get(),
           self.sub5var.get(),
           self.sub6var.get(),
           self.scorevar.get(),
           self.semvar.get()
           ))
        except: 
           messagebox.askretrycancel("Error" , "the infomation you entred is not complited")
        
        lo.commit()
        self.comeback_sub()#------show before Exit -------
        lo.close()
    
    def add_teacher(self):
                 #-------ad var to connect by pymysql------
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
        cur1=lo.cursor()
        #try:
        cur.execute('insert into teacher (id,name,date,nation,qualification,gender,phone,city,address,career,seat) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.seriesvar.get(),
           self.teachervar.get(),
           self.datevar.get(),
           self.nationvar.get(),
           self.qualivar.get(),
           self.nationvar.get(),
           self.phonevar.get(),
           self.cityvar.get(),
           self.addressvar.get(),
           self.careervar.get(),
           self.seatsvar.get()
           ))
        cur1.execute('insert into teacher_table (id,teacher,curse,password) values (%s,%s,%s,%s)',(self.seriesvar.get(),self.teachervar.get(),self.careervar.get(),'0000'))
        #except: 
             #messagebox.askretrycancel("Error" , "!رقم التسلسل موجود أو المادة المدخلة متكررة ")

          
        lo.commit()
        self.comeback_teacher()#------show before Exit -------
        lo.close()

    #---------to show Data---------
    def comeback(self):
        come=mysql.connector.connect(host='localhost',user='root',password='#User#Root:#123',database='studentdb')
        do=come.cursor()
        bee=come.cursor()
        bee.execute=('select name date nation watani gender phone city address from student ordered by id')
        do.execute('select id ,name, date, nation, watani, gender, phone, city, address from students')
        rows= do.fetchall()#-----bring all data-----
        if len(rows)!=0:
            self.student.delete(*self.student.get_children())
            for row in rows:#---------loop for bring it up to the table-------
                self.student.insert('',END,values=row)
            come.commit()
        come.close()
        
    def comeback_sub(self):
        come=mysql.connector.connect(host='localhost',user='root',password='#User#Root:#123',database='studentdb')
        do=come.cursor()
        do.execute('select * from courses')
        rows= do.fetchall()#-----bring all data-----
        if len(rows)!=0:
            self.curse.delete(*self.curse.get_children())
            for row in rows:#---------loop for bring it up to the table-------
                self.curse.insert('',END,values=row)
            come.commit()
        come.close()        

    def comeback_teacher(self):
        come=mysql.connector.connect(host='localhost',user='root',password='#User#Root:#123',database='studentdb')
        do=come.cursor()
        do.execute('select * from teacher')
        rows= do.fetchall()#-----bring all data-----
        if len(rows)!=0:
            self.teacher.delete(*self.teacher.get_children())
            for row in rows:#---------loop for bring it up to the table-------
                self.teacher.insert('',END,values=row)
            come.commit()
        come.close()           

    def delete(self):         
         dele=mysql.connector.connect(
             host='localhost',
             user='root',
             password='#User#Root:#123',
             database='StudentDB')
         do0=dele.cursor()
         do1=dele.cursor()
         do2=dele.cursor()
         do3=dele.cursor()
         cur=dele.cursor()
         #------------------------focus in this----------------------
         try:
           cur.execute("select num from students where id= %s LIMIT 1",(self.idvar.get(),))
           k=cur.fetchone()
           k = k[0]       
           do1.execute('delete from courses where id=' + self.idvar.get())
           do0.execute('DELETE FROM students WHERE id='+ self.idvar.get())
           do2.execute('delete from score_table where num =' + str(k))
           do3.execute('delete from subject_table where num =' + str(k))    
           dele.commit()
           self.comeback()#----to delete directly----
           dele.close()
         except:
            messagebox.askretrycancel("Error" , "! الطالب غير موجود")
 
    def delete_teacher(self):    
                         
         dele=mysql.connector.connect(
             host='localhost',
             user='root',
             password='#User#Root:#123',
             database='StudentDB')
         do0=dele.cursor()
         do1=dele.cursor()
         #-------focus in this-----
         #do.execute('delete from students where name=' + self.delevar.get())
         do0.execute('DELETE FROM teacher WHERE id='+ self.seriesvar.get())
         do1.execute('DELETE FROM teacher_table WHERE id='+ self.seriesvar.get())
         #do.execute('delete from students where phone=' + self.delevar.get())
            
         dele.commit()
         self.comeback_teacher()#----to delete directly----
         dele.close()

    def delete_subject(self):
        do = delete_sub.DELETE()
    #----------------------delet fields------
    def clear(self):
          self.idvar.set('')
          self.namevar.set(''),
          self.datevar.set(''),
          self.nationvar.set(''),
          self.watanivar.set(''),
          self.gendervar.set(''),
          self.phonevar.set(''),
          self.cityvar.set(''),
          self.addressvar.set('')

    def clear_sub(self):
          self.idvar.set('')
          self.namevar.set(''),
          self.sub1var.set(''),
          self.sub2var.set(''),
          self.sub3var.set(''),
          self.sub4var.set(''),
          self.sub5var.set(''),
          self.sub6var.set(''),
          self.semvar.set(''),
          self.scorevar.set('')     

    def clear_teacher(self):
          self.seriesvar.set('')
          self.teachervar.set(''),
          self.datevar.set(''),
          self.nationvar.set(''),
          self.qualivar.set(''),
          self.gendervar.set(''),
          self.phonevar.set(''),
          self.cityvar.set(''),
          self.addressvar.set(''),
          self.careervar.set('')    
          self.seatsvar.set('')                  
              
    #-----------------------events----------------
    def mycursor(self,ev):#ev is your event that have everything 
         info=self.student.focus()
         contents=self.student.item(info)
         row=contents['values']
         self.idvar.set(row[0])
         self.namevar.set(row[1])
         self.datevar.set(row[2])
         self.nationvar.set(row[3])
         self.watanivar.set(row[4])
         self.gendervar.set(row[5])
         self.phonevar.set(row[6])
         self.cityvar.set(row[7])
         self.addressvar.set(row[8])
    
    def mycursor_sub(self,ev):#ev is your event that have everything 
         info=self.curse.focus()
         contents=self.curse.item(info)
         row=contents['values']
         self.idvar.set(row[0])
         self.namevar.set(row[1])
         self.sub1var.set(row[2])
         self.sub2var.set(row[3])
         self.sub3var.set(row[4])
         self.sub4var.set(row[5])
         self.sub5var.set(row[6])
         self.sub6var.set(row[7])
         self.scorevar.set(row[9])  
         self.semvar.set(row[10])                     

    def mycursor_teacher(self,ev):#ev is your event that have everything 
         info=self.teacher.focus()
         contents=self.teacher.item(info)
         row=contents['values']
         self.seriesvar.set(row[0])
         self.teachervar.set(row[1])
         self.datevar.set(row[2])
         self.nationvar.set(row[3])
         self.qualivar.set(row[4])
         self.gendervar.set(row[5])
         self.phonevar.set(row[6])
         self.cityvar.set(row[7])
         self.addressvar.set(row[8])
         self.careervar.set(row[9])
         self.seatsvar.set(row[10])

    def Pass_student(self):
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
        try:
           cur.execute('update students set password = "0000" where id =' + self.idvar.get())
        except:
            messagebox.askretrycancel("Error" , " !اختر الطالب المراد اعادة تعيين كلمة السر له ")
        lo.commit()
        lo.close() 

    def Pass_teacher(self):
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
        cur=lo.cursor()
        try:
           cur.execute('update teacher_table set password = "0000" where id =' + self.seriesvar.get())
        except:
            messagebox.askretrycancel("Error" , " !اختر المعلم المراد اعادة تعيين كلمة السر له ")
        lo.commit()
        lo.close()        
    #----------------------updates-----------
    def update_sub(self):
        update=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='StudentDB'
            )
        change=update.cursor()
        change1=update.cursor()
        change.execute('update courses set name=%s,subject1=%s,subject2=%s,subject3=%s,subject4=%s ,subject5=%s,subject6=%s, pecent=%s,coursescol=%s where ID=' + self.idvar.get() ,(
          self.namevar.get(),
          self.sub1var.get(),
          self.sub2var.get(),
          self.sub3var.get(),
          self.sub4var.get(),
          self.sub5var.get(),
          self.sub6var.get(),
          self.scorevar.get(),
          self.semvar.get()          
         ))
        tup=self.namevar.get()
        change1.execute('update students set name=%s where id ='+ self.idvar.get(),(tup[0],))
        update.commit()
        self.comeback_sub()#------show before Exit -------
        update.close()

    def update(self):
        update=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='StudentDB'
            )
        change=update.cursor()
        change1=update.cursor()
        change.execute('update students set id=%s, name=%s,date=%s,nation=%s,watani=%s,gender=%s ,phone=%s,city=%s,address=%s where ID=' + self.idvar.get() ,( self.idvar.get(),
          self.namevar.get(),
          self.datevar.get(),
          self.nationvar.get(),
          self.watanivar.get(),
          self.gendervar.get(),
          self.phonevar.get(),
          self.cityvar.get(),
          self.addressvar.get()
         ))
        tup=[self.namevar.get()]
        change1.execute('update courses set name=%s where id ='+ self.idvar.get(),[tup[0]])         
        update.commit()
        self.comeback()#------show before Exit -------
        self.clear()
        update.close()    

    def update_teacher(self):
        update=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='StudentDB'
            )
        change=update.cursor()
        c=update.cursor()
        change.execute('update teacher set name=%s,date=%s,nation=%s,qualification=%s,gender=%s ,phone=%s,city=%s,address=%s , career=%s , seat=%s where id=' + self.seriesvar.get() ,(
          self.teachervar.get(),
          self.datevar.get(),
          self.nationvar.get(),
          self.qualivar.get(),
          self.gendervar.get(),
          self.phonevar.get(),
          self.cityvar.get(),
          self.addressvar.get(),
          self.careervar.get(),
          self.seatsvar.get()
         ))
        c.execute('update teacher_table set teacher=%s, curse=%s where id=' + self.seriesvar.get() ,(self.teachervar.get(),self.careervar.get()))
        update.commit()
        self.comeback_teacher()#------show before Exit -------
        self.clear_teacher()
        update.close()    

    #----------------search def--------------              
    def search(self):
        con=mysql.connector.connect(host='localhost',user='root',password='#User#Root:#123',database='StudentDB')
        do=con.cursor()
        try:
                do.execute("select * from students where " +
                str(self.sby.get())+" LIKE '%" +str(self.svar.get())+"%'")#----link combo with entry-----
                rows= do.fetchall()#-----bring all data-----
                if len(rows)!=0:
                   self.student.delete(*self.student.get_children())
                else:
                    messagebox.askretrycancel("error","the student not found! ")
                for row in rows:#---------loop for bring it up to the table-------
                   self.student.insert('',END,values=row)
        except:
             messagebox.askretrycancel("error","the datatype is not matched ")
                
        con.commit()
        con.close()
   
    #-----------------about us--------------    
    def abt(self):
            messagebox.showinfo("About US!", 'we are a team of university student developers. \n Thanks For Your Supports')
    
    def back(self):  #-------------------------------back Clear-----------------------------------
        self.stu.destroy()
        self.stu.update()

    def refresh(self):
        try:
           self.comeback()
           self.clear()
        except:
            messagebox.askretrycancel('Error','الرجاء اتباع التعليمات !')              
                     