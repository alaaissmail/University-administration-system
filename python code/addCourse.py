class CourseNode:
    def __init__(self, code, credits, prerequisites):
        self.code = code
        self.credits = credits
        self.prerequisites = prerequisites
        self.grade = None
        self.left = None
        self.right = None

class CourseBST:
    def __init__(self):
        self.root = None
        self.current_semester_credits = 0
        self.total_credits = 0
        self.max_credits_per_semester = 18
        self.courses_added = []

    def insert(self, code, credits, prerequisites): #insert new course
        new_course = CourseNode(code, credits, prerequisites)
        if self.root is None:
            self.root = new_course
        else:
            self._insert(self.root, new_course)

        return [code, credits, prerequisites]

    def _insert(self, current, new_course):
        if new_course.code < current.code:
            if current.left is None:
                current.left = new_course
            else:
                self._insert(current.left, new_course)
        else:
            if current.right is None:
                current.right = new_course
            else:
                self._insert(current.right, new_course)


    def search(self, code):  #Search for a course by its code
        return self._search(self.root, code)

    def _search(self, current, code):
        if current is None:
            return None
        if current.code == code:
            return current
        elif code < current.code:
            return self._search(current.left, code)
        else:
            return self._search(current.right, code)

    def check_prerequisites(self, course_code, student_grades):
        course = self.search(course_code)
        if course is None:
            print(f"Course {course_code} not found.")
            return False
        
    def check_prerequisites1(self, course_code):
        course = self.search(course_code)
        if course is None:
            print(f"Course {course_code} not found.")
            return False    

        for prereq_code in course.prerequisites:
            prereq_course = self.search(prereq_code)
            if prereq_course is None or student_grades.get(prereq_code) is None:
                print(f"Prerequisite {prereq_code} not completed.")
                return False
            elif student_grades[prereq_code] < 50:
                print(f"Failed prerequisite {prereq_code} with grade {student_grades[prereq_code]}.")
                return False

        return True

    def add_course(self, course_code, student_grades):#=============================work home=======================
        course = self.search(course_code)
        if course is None:
            print(f"Course {course_code} not found.")
            return

        if self.check_prerequisites(course_code, student_grades):
            if self.current_semester_credits + course.credits > self.max_credits_per_semester:
                print(f"Cannot add course {course_code}. Credit limit of 18 exceeded.")
            else:
                print(f"Course {course_code} added.")
                self.current_semester_credits += course.credits
                self.courses_added.append(course)
        else:
            print(f"Cannot add course {course_code}. ")

    def cridits(self,course_code):
        course = self.search(course_code)
        if self.check_prerequisites1(course_code):
                self.current_semester_credits += course.credits
                self.courses_added.append(course)

        
    def delete_course(self, course_code):
        course = self.search(course_code)
        if course is None:
            print(f"Course {course_code} not found.")
            return

        for i, courses_added in enumerate(self.courses_added):
            if courses_added.code == course_code:
                print(f"Course {course_code} removed.")
                self.courses_added.pop(i)
                self.current_semester_credits -= course.credits
                self.total_credits -= course.credits
                print(f"Current semester total credits: {self.current_semester_credits}")
                return

        print(f"Course {course_code} not found in added courses.")

    def calculate_general_average(self):
        total_grade = 0
        total_credits = 0

        for course in self.courses_added:
            if course.grade is not None:
                total_grade += course.grade * course.credits
                total_credits += course.credits

        if total_credits == 0:
            print("No courses completed to calculate the average.")
            return 0

        general_average = total_grade / total_credits
        print(f"General Average: {general_average:.2f}")
        return general_average

    def final_grades(self, course_grades):
        for course_code, grade in course_grades.items():
            course = self.search(course_code)
            if course:
                course.grade = grade

    def add_ee599(self):
        if self.total_credits >= 128 and student_grades[prereq_code] > 50 :
            print("Course EE599 added.")
            self.add_course('EE599', {})
        else:
            print("Cannot add EE599. Total credits less than 128.")


course_bst = CourseBST()
courses_to_insert = [
['GS200', 3, ['GS102']],
    ['EE200', 3, ['GS102','GS112']],
    ['EE201', 2, ['EE200']],
    ['EE202', 3, ['EE200','GS112']],
    ['EE219', 3, ['EE200']],
    ['EE234', 3, ['GS102']],
    ['EE302', 3, ['EE202','GS204']],
    ['EE303', 3, ['GS200','GS203','GS204']],
    ['EE304', 3, ['EE200','EE219','EE234']],
    ['EE311', 2, ['EE201','EE219','EE319']],
    ['EE313', 3, ['EE200', 'GS203','GS204']],
    ['EE316', 3, ['EE302','GS204']],
    ['EE319', 3, ['EE202','EE219']],
    ['EE331', 2, ['EE201','EE234']],
    ['EE334', 3, ['EE234','GS200']],
    ['EE342', 3, ['EE202']],
    ['EE352', 3, ['EE202']],
    ['EE362', 3, ['EE302']],
    ['EE413', 3, ['EE313']],
    ['EE416', 3, ['EE316','GS206']],
    ['EE419', 3, ['EE319']],
    ['EE421', 2, ['EE304','EE311','EE331','EE316']],
    ['EE423', 3, ['EE302','EE319']],
    ['EE429', 3, ['EE319']],
    ['EE432', 3, ['EE334']],
    ['EE433', 3, ['EE334']],
    ['EE434', 3, ['EE334']],
    ['EE442', 3, ['EE342']],
    ['EE443', 3, ['EE342','EE352','ME210']],
    ['EE445', 3, ['EE342']],
    ['EE446', 3, ['EE342', 'EE352']],
    ['EE448', 3, ['EE342','EE219']],
    ['EE449', 3, ['EE352']],
    ['EE451', 2, ['EE304','EE311','EE331']],
    ['EE452', 3, ['EE352']],
    ['EE461', 3, ['EE304','EE311','EE331','EE362']],
    ['EE462', 3, ['EE362']],
    ['EE463', 3, ['EE334','EE362']],
    ['EE491', 3, ['EE461']],
    ['EE513', 3, ['EE413']],
    ['EE516', 3, ['EE416']],
    ['EE519', 3, ['EE429']],
    ['EE521', 2, ['EE421','EE416','EE419']],
    ['EE524', 3, ['EE416']],
    ['EE526', 3, ['EE416']],
    ['EE532', 3, ['EE303','EE434']],
    ['EE535', 3, ['EE434','EE462']],
    ['EE542', 3, ['EE442']],
    ['EE548', 3, ['EE448']],
    ['EE551', 2, ['EE451','EE448','EE449']],
    ['EE552', 3, ['EE452']],
    ['EE561', 3, ['EE461','EE462','EE463']],
    ['EE562', 3, ['EE303','EE462']],
    ['EE563', 3, ['EE303','EE462']],
    ['EE599', 3, ['EE491']]
]

inserted_courses = []

# Loop through and insert each course into the tree, and store the course details
for course in courses_to_insert:
    code, credits, prerequisites = course
    course_details = course_bst.insert(code, credits, prerequisites)
    inserted_courses.append(course_details)

# Output the list of all inserted courses


if __name__ == '__main__':
    student_grades = {
        'GS102': 55,
        'EE334': 30,
        'GS200': 60,
        'EE200': 65,
        'EE202': 58,
        'EE234': None,
        'EE302': 70,
    }

    course_bst.add_course('EE219')
    course_bst.add_course('EE432')
    course_bst.add_course('EE434')
    course_bst.add_course('EE362')
    course_bst.add_course('EE201')

    course_bst.final_grades(student_grades)

    print(f"Total credits for the current semester: {course_bst.current_semester_credits}")
    print(f"Total credits (all semesters): {course_bst.total_credits}")

    course_bst.calculate_general_average()
    course_bst.delete_course('EE201')



