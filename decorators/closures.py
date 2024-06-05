"""closures are dynamically created func that are returned by outer function as a inner function object
 and the function object takes a snapshot of all the variables,arguments and names in its(inner funct) containing scope."""

def outer_func(xx):
    show = 'local variable'
    print("testing outer function scope")
    def inner_func():
        print("this is argument from outer function and printing from inner func", xx)
        print(show, ',,variable in outer function scope')
    return inner_func
    
sample_1 = outer_func("kundanhur nizam")

sample_1()

"""case 2"""
#adding 2 numbers

def outer(x):
    def inner(y):
        return x + y
    return inner

test = outer(3) #here we returned the inner function object to the variable and also we called the outer function...=> 3 is x
print(test(6)) # y is 6