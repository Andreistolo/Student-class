class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone 
        self.course = course
        self.index_number = index_number


    def getInfo(self):
        print("Student information: ",self.name, "Address: ", self.address, "Phone number: ", 
        self.phone, "Course taken: ", self.course, "Index number: ", self.index_number)


Student1 = Student("Andrei Necule", "Strada Nr.1", "07171717", "Python 101", 12345)
Student1.getInfo()

Student2 = Student("Robert Mizai", "Strada Nr.2", "0727272", "Java 202", 24689)
Student2.getInfo()

Student3 = Student("Sanda Prada", "Strada Nr.3", "07373737", "HTML 303", 35788)
Student3.getInfo()

       