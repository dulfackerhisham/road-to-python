"""single inheritance"""
class A:
    def feature1(self):
        print('this is fesature 1 from class A')

    def feature2(self):
        print('this is feature 2 from class A')

# a = A()
# a.feature1()
# a.feature2()

class B(A):
        
    # def feature1(self):
    #     print('this is fesature 1 from class B')

    # def feature2(self):
    #     print('this is feature 2 from class B')

    def feature3(self):
        print('this is fesature 3 from class B')

    def feature4(self):
        print('this is feature 4 from class B')

b = B()
b.feature2()
b.feature1()
b.feature3()
b.feature4()

