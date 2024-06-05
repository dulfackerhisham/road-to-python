class Student():
    """self => 1st argument is self which means 1st argument is instance.self represents instances of class"""

    school = 'shathi al noor' #class variable
    scholarship = 5000

    def __init__(self,fname,lname,roll_no,grade):
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no
        self.grade = grade

    def __str__(self) -> str:
        return self.fname + ' roll no:' + str(self.roll_no)

    def show(self):
        return f"My name is {self.fname + ' ' + self.lname}. im studying in {self.grade} and my roll number is {self.roll_no}.school is {self.school}"
    
    def skul(self):
        return self.school
    
    @classmethod
    def set_scholrship(cls, amount):
        cls.scholarship = amount

std1 = Student('hisham', 'dulfacker', 27, 12)
std2 = Student('izu', 'mown', 12, 2)

std2.school = 'thss'

Student.set_scholrship(10000)
print(std1.show())
print(std2.show())
# print(std1.skul())
print(Student.scholarship)