class A:
    def feature1(self):
        print("f1 of class A")

    def common_feature(self):
        print("common feature from class A")

class B:
    def feature2(self):
        print("f2 of class B")

    def common_feature(self):
        print("common feature from class B")

class Ab:
    def sep_feature(self):
        print("class Ab sepearate feature")

class C(B,A,Ab):
    def feature1(self):
        print('f3 of class C')
        super().feature1()

c = C()
c.feature1()
c.feature2()
# c.feature3()
c.common_feature()
c.sep_feature()