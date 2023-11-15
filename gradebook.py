from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = birth_date
        self.alive = AliveStatus.ALIVE

    def update_first_name(self, name_to_use: str):
        self.first_name = name_to_use

    def update_last_name(self, name_to_use: str):
        self.last_name = name_to_use

    def update_dob(self, birth_date):
        self.dob = birth_date

    def update_status(self, alive_status: AliveStatus):
        self.alive = alive_status


class Instructor(Person):

    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self.instructor_id = f'Instructor_{uuid4()}'


class Student(Person):

    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self.student_id = f'Student_{uuid4()}'


class ZipCodeStudent(Student):

    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self.student_id = f'Student_{uuid4()}'


class HighSchoolStudent(Student):

    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self.student_id = f'Student_{uuid4()}'


class Classroom:

    def __init__(self):
        self.instructors = []
        self.students = []

    def add_instructor(self, instructor_id):
        self.instructors.append(instructor_id)

    def remove_instructor(self, instructor_id):
        self.instructors.remove(instructor_id)

    def add_student(self, student_id):
        self.students.append(student_id)

    def remove_student(self, student_id):
        self.students.remove(student_id)

    def print_instructors(self):
        print(f'The instructors for {self} are: ')
        for instructor in self.instructors:
            print(f'Instructor: {instructor.first_name} {instructor.last_name}')

    def print_students(self):
        print(f'The students for {self} are: ')
        for student in self.students:
            print(f'Student: {student.first_name} {student.last_name}')
