class A:
    def greet1(self):
        print("class A greetings 1")

class B(A):
    def greet1(self):
        print('class B greet 1')
        # return super().greet1()
    
    def greet2(self):
        print('class B greet 2')

class C(B):

    def greet1(self):
        print('class C greet 1')
        # return super().greet1()

    def greet3(self):
        print('class C greet 3')
    
b = B()
# b.greet1()
# b.greet2()

c = C()
c.greet1()
c.greet2()
c.greet3()