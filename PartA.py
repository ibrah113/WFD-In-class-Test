class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.DoB}")
        print(f"Sex: {self.sex}")
        print(f"Staff ID: {self.staffID}")
        print(f"Address: {self.address}")

    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Invalid type for name")

    def update_DoB(self, new_DoB):
        if isinstance(new_DoB, str):  
            self.DoB = new_DoB
        else:
            print("Invalid type for DoB")

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Invalid type for sex")

    def update_staffID(self, new_staffID):
        if isinstance(new_staffID, int):
            self.staffID = new_staffID
        else:
            print("Invalid type for staffID")

    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address
        else:
            print("Invalid type for address")
    
class Teacher(Staff):
    def __init__(self, name, DoB, sex, staffID, address, subject, years_experience):
        super().__init__(name, DoB, sex, staffID, address)
        self.subject = subject
        self.years_experience = years_experience

def print_teacher_info(self):
        super().print_info()
        print(f"Subject: {self.subject}")
        print(f"Years of Experience: {self.years_experience}")
