import unittest
from PartA import Staff, Teacher

# Task B2 - Test if an object is an instance of a class
class TestStaffTeacher(unittest.TestCase):

    def test_is_instance_of_staff(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        self.assertIsInstance(staff1, Staff)  

    def test_is_instance_of_teacher(self):
        teacher1 = Teacher("Ibrahim Shaban", "11/03/2004", "Male", 1002, "Tud Blanch", "Mathematics", 8)
        self.assertIsInstance(teacher1, Teacher)  

    def test_is_not_instance_of_teacher(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        self.assertNotIsInstance(staff1, Teacher)  

    def test_is_not_instance_of_staff(self):
        teacher1 = Teacher("Ibrahim Shaban", "11/03/2004", "Male", 1002, "Tud Blanch", "Mathematics", 8)
        self.assertNotIsInstance(teacher1, Staff)  


