import unittest
from PartA import Staff, Teacher

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

    def test_objects_are_identical(self):
        staff1a = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1b = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        self.assertEqual(staff1a.name, staff1b.name)  
        self.assertEqual(staff1a.staffID, staff1b.staffID)  

    def test_objects_are_not_identical(self):
        staff1a = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff2 = Staff("Ryan Smith", "20/10/2003", "Male", 1003, "Castlegrange Park")
        self.assertNotEqual(staff1a.name, staff2.name)  
        self.assertNotEqual(staff1a.staffID, staff2.staffID)  

    def test_update_name(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1.update_name("Ryan Smith")
        self.assertEqual(staff1.name, "Ryan Smith")  

    def test_update_address(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1.update_address("3 Castlegrange Park")
        self.assertEqual(staff1.address, "3 Castlegrange Park")  

    def test_update_DoB(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1.update_DoB("01/01/2000")
        self.assertEqual(staff1.DoB, "01/01/2000") 

    def test_update_sex(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1.update_sex("Female")
        self.assertEqual(staff1.sex, "Female")  

    def test_update_staffID(self):
        staff1 = Staff("Mike Kazakovas", "15/04/2004", "Male", 1001, "Tud Blanch")
        staff1.update_staffID(1005)
        self.assertEqual(staff1.staffID, 1005)  

if __name__ == "__main__":
    unittest.main()
