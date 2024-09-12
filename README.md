# University-administration-system
It is designed to simplify the management of student data, courses, and academic performance.
It allows university administrators to add, update and delete courses and register students and teachers. 
It can view the teaching plan and schedules.
It also allows students to add and delete courses and allows teachers to add grades for each student. The system also allows updating results for specific courses, ensuring accurate record keeping.

![uotlogo](https://github.com/user-attachments/assets/cc7600e2-9066-4a8a-8bac-0543e9d9c026)


## Installation

Install MySQL

```bash
  1. You can download MySQL from [the official MySQL website] (https://dev.mysql.com/downloads/installer/).
  2. Follow the installation instructions for your operating system (Windows, macOS, or Linux).
  3. open MySQL -> click on MySQL connections.
  4. Enter username 'root' and password '#User#Root:#123'
  5. select execute from this window 
  ```
![Screenshot 2024-09-12 213650](https://github.com/user-attachments/assets/e34591ea-117c-48be-ad6d-50d040b59d68)
 ```bash
open the Database, and follow the first comment in Login file
```
  open Tkinter
  ```bash
  1. In command line terminal write pip install (name of package)
  2. you have to install these packages to work the Tkinter in python:
  -tkinter
  -Pillow
  -PIL image ,ImageTk
  -tkcalendar
  -mysql.connetor
  -messagebox
  -tkcalendar
  -DateEntry
  -webbrowser
```
if you could not get this, you can open this [link](https://www.python.org/) and download these packages


setup VS code
Download from (https://code.visualstudio.com/download)

    

## Libraries and Dependencies

-The following Python libraries are required to run this project:
- Tkinter: For building the graphical user interface.
- MySQL Connector: To connect and interact with the MySQL database.
- VS Code: to coding in Python.

## Technologies

- Python on VS Code.
- MySQL.

## Features
- Admin Management: assign new teachers and students and thier courses.
- Student Management: Add, update, and delete student records.
- Course Management: Assign and manage courses for students.
- Grades Management: Update and view student grades for each course by Teacher.
- Database: Use MySQL for secure and scalable data storage.
- Data Security: Ensure the security and privacy of student and faculty data.


## Usage/Examples

## Some knowledge about the system

What admin can do:
- add, update and delete student.
- add, update and delete teacher information and assign teacher to course.
- add and delete courses to students.
- show the informations of all students and teachers.
- show students's courses.

what students can do:
- add and delete courses.
- view the study and exams schedles
- show the teaching plan for some courses.
- can study from online courses in Stream UOT.
- can show the table of courses and calculate the credits and grades.

what teachers can do:
- add grades for thier students.


### To use the University Administration System, follow these steps:
- open photo file in github and copy the link photo school, paste it in login file in Line 67
- the same steps in other lines of each file, follow the comment and change the link of the photos:
- student432: line 177 , line 188 , line 328 , line 340
- teacher432:line 134
- Admin1: line 90

## Login window
![Screenshot 2024-09-12 215605](https://github.com/user-attachments/assets/096af848-b25a-4e4f-b57d-d5a0da434493)
## login as an Admin
- run Login file, you can login as an admin, teacher and student. once you want login as an admin you should enter:

```bash
username: Nuri BenBarka
password: 1234

```
- Here, the admin can add student information and add courses also can add teacher information.
  ![Screenshot 2024-09-12 125720](https://github.com/user-attachments/assets/a1712757-9285-4c16-8793-4a3cc3bf87e5)

After adding student information, it will be stored in command students informations you can easily show it.

open students courses, insert name and ID number of student that you want to add courses and chose any course press add.
![Screenshot 2024-09-12 221942](https://github.com/user-attachments/assets/e2bf6cbb-47b0-49ae-ad11-0c75531ccbbc)

if you want to update or edit course you can change and add one course or group of courses at the same time.

if you want to delete course just press delete, it will show a window, input ID of course and the name of course then delete.

you can also calculate the credits of the semester. 

please input the general average %

Note: when a course is deleted, the admin should exit the system and open again to calculate number of credits correctly!

The student has been added to the teacher's course Successfully!

-open teachers informations to add new teacher information and you can assign teacher to course, However, The serial number cannot be repeated, and you cannot add teachers to the same course.
![Screenshot 2024-09-12 215817](https://github.com/user-attachments/assets/95ce86f4-6a70-4258-8846-60c389cf23e8)

if you want to delete a teacher just click on the teacher and delete.
if you want to edit teacher information click on the teacher and edit it.

## login as a Student
- run Login file, you can login as student you should enter:
```bash
username : 'student ID'
password: by default '0000'
```
-you can change the password by click change the password.

## student window
![Screenshot 2024-09-12 220128](https://github.com/user-attachments/assets/0f92ebe5-e948-4c8d-ba48-32e1d53961c9)

if you want to add a course press add courses and add the course you want, but you cannot add courses if your credits greater than 18 credits, the system will not allow you to add courses that has dependencies on each other (prerequisites courses).


- you can show your courses after added, and there are Teaching Plans for some courses like [EE432, EE434, EE303, EE319, EE302, EE304]
## grades added by teacher
![Screenshot 2024-09-12 222751](https://github.com/user-attachments/assets/5f2f56c2-cc02-4d28-9dd0-896794c512ce)

- you can study all your courses by press Stream UOT -> online courses.

- you have the study and the exams schedules.

## login as a Teacher
 - run Login file, you can login as student you should enter:
```bash
username : 'teacher name '
password: by default '0000'

```
-you can change the password by click change the password.


after login you will find all students that already added in your course, then you can add attendce, midterm and final grades to your students.
![Screenshot 2024-09-12 131405](https://github.com/user-attachments/assets/b2110382-a808-419b-aed7-68437b31cc93)

the system will calculate the total grade of the course and insert the evaluation.

if there is number of seats lets say 90 seats, and 100 students want to add the course, this problem can be solved by using Heap because it takes the priority:
```bash
import heapq

students = [
    (85%, 'student_2'), (90%, 'student_1'), (70%, 'student_3'),
]

course_seats = []
for student in students:
    heapq.heappush(course_seats, student)
    if len(course_seats) > 90:
        heapq.heappop(course_seats)  

for priority, student_id in course_seats:
    print(f"{student_id} ")
```
## Acknowledgements

 University administration system was created by:
  **[Alaa ismail](https://github.com/alaaissmail)** and
 **[Sorour Saed](https://github.com/SorourMSaed)** and 
   **[Rasha Elwafi](https://github.com/elwafi2000)**.

   ## Contact
if you have any questions Hit me up!

Alaa ismail - ismail@alaa.ly

Project Link: [University administration system ](https://github.com/alaaissmail/University-administration-system.git)
