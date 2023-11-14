import unittest


class TestGradebookPerson(unittest.TestCase):

    def test_update_first_name(self):
        expected = True
        actual = False
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_last_name(self):
        expected = True
        actual = False
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_dob(self):
        expected = True
        actual = False
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_status(self):
        expected = True
        actual = False
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
