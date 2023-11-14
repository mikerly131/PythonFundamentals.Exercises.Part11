import unittest
import gradebook

class TestGradebookPerson(unittest.TestCase):

    def setUp(self):
        self.test_person1 = gradebook.Person('Bob', 'Jones', '2/23/2002')
        self.test_person2 = gradebook.Person('Jen', 'Lupin', '9/23/1984')

    def test_update_first_name(self):
        expected = "Rodger"
        self.test_person1.update_first_name("Rodger")
        actual = self.test_person1.first_name
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_last_name(self):
        expected = "Greenwood"
        self.test_person1.update_last_name("Greenwood")
        actual = self.test_person1.last_name
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_dob(self):
        expected = "12/30/1984"
        self.test_person2.update_dob("12/30/1984")
        actual = self.test_person2.dob
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_status(self):
        expected = gradebook.AliveStatus.DECEASED
        self.test_person2.update_status(gradebook.AliveStatus.DECEASED)
        actual = self.test_person2.alive
        self.assertEqual(expected, actual)  # add assertion here


class TestClassRoom(unittest.TestCase):

    def test_add_instructor(self, instructor_id):
        self.instructors.append(instructor_id)

    def test_remove_instructor(self, instructor_id):
        self.instructors.pop(instructor_id)

    def add_student(self, student_id):
        self.students.append(student_id)

    def remove_student(self, student_id):
        self.students.pop(student_id)

    def print_instructors(self):
        print(f'The instructors for {self} are: ')
        for instructor in self.instructors:
            print(f'Instructor: {instructor.first_name} {instructor.last_name}')

    def print_students(self):
        print(f'The students for {self} are: ')
        for student in self.students:
            print(f'Student: {student.first_name} {student.last_name}')


if __name__ == '__main__':
    unittest.main()
