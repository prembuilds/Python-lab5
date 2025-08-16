class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Ankit", 85)
s2 = Student("Riya", 92)
s3 = Student("Kiran", 78)

s1.show_details()
s2.show_details()
s3.show_details()
