import unittest
import gradebook
import io
import unittest.mock


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
        expected = "DECEASED"
        self.test_person2.update_status("DECEASED")
        actual = self.test_person2.alive
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_status2(self):
        expected = "ALIVE"
        self.test_person2.update_status("ALIVE")
        actual = self.test_person2.alive
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_status3(self):
        expected = gradebook.AliveStatus.DECEASED
        self.test_person1.update_status(gradebook.AliveStatus.DECEASED)
        actual = self.test_person1.alive
        self.assertEqual(expected, actual)  # add assertion here

    def test_update_status4(self):
        expected = gradebook.AliveStatus.ALIVE.name
        self.test_person1.update_status("ALIVE")
        actual = self.test_person1.alive
        self.assertEqual(expected, actual)  # add assertion here


class TestClassRoom(unittest.TestCase):

    def setUp(self):
        self.test_classroom = gradebook.Classroom()
        self.test_person3 = gradebook.Student('Bob', 'Jones', '2/23/2002')
        self.test_person4 = gradebook.Instructor('Jen', 'Lupin', '9/23/1984')
        self. test_person5 = gradebook.Instructor('Larry', 'Trailmix', '3/18/1968')
        self.test_person6 = gradebook.Student('Chelsea', 'Ladyperson', '12/23/1992')

    def test_add_instructor(self):
        expected = self.test_person4.instructor_id
        self.test_classroom.add_instructor(expected)
        actual = self.test_classroom.instructors[0]
        self.assertEqual(expected, actual)  # add assertion here

    def test_remove_instructor(self):
        expected = self.test_person5.instructor_id
        test_ins = self.test_person4.instructor_id
        self.test_classroom.add_instructor(test_ins)
        self.test_classroom.add_instructor(expected)
        self.test_classroom.remove_instructor(test_ins)
        actual = self.test_classroom.instructors[0]
        self.assertEqual(expected, actual)  # add assertion here

    def test_add_student(self):
        expected = self.test_person3.student_id
        self.test_classroom.add_student(expected)
        actual = self.test_classroom.students[0]
        self.assertEqual(expected, actual)  # add assertion here

    def test_remove_student(self):
        expected = self.test_person3.student_id
        test_stu = self.test_person6.student_id
        self.test_classroom.add_student(test_stu)
        self.test_classroom.add_student(expected)
        self.test_classroom.remove_student(test_stu)
        actual = self.test_classroom.students[0]
        self.assertEqual(expected, actual)  # add assertion here

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_instructors(self, mock_stdout):
        self.test_classroom.add_instructor(self.test_person4.instructor_id)
        self.test_classroom.add_instructor(self.test_person5.instructor_id)
        expected = 'The instructors for <gradebook.Classroom object at 0x1010d10a0> are: \nInstructor: Jen Lupin\nInstructor: Larry Trailmix\n'
        self.test_classroom.print_instructors()
        self.assertEqual(expected, mock_stdout.getvalue())



    def test_print_students(self):
        expected = 'The students for test_classroom are: \nStudent: Bob Jones\n'



if __name__ == '__main__':
    unittest.main()
