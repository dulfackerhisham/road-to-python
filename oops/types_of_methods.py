class Student:
    school = 'Dodge'

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod #class method => passing class as 1st argument
    def info(cls):
        return cls.school
    @staticmethod
    def s_info(): #static method => is not related to object or class..THE METHOD WHICH HAS NOTHING TO DO WITH CLASS VARIABLE AND INSTANCE VARIABLE
         print('this is static method')
    
s1 = Student(80, 76, 95)
s2 = Student(98, 99, 78)

print(s2.avg()) #this avg() is instance method => it works with object...
                #fetching the value of instance variable = accessor methods
                #modifying value of instance variable= mutators methods

print(Student.info()) #class method

Student.s_info() #static method
