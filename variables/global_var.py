#GLOBAL VARIABLES

# step 1
# global_var = 1234

# def testing():
#     global_var = "local variable"
#     print(global_var)

# print(global_var)
# testing()

# step 2
glob_var = "test 2"

def test2():
    global glob_var
    glob_var = " local var to global variable"
    print(f"called from inside function'{glob_var}'")

test2()
print(f"{glob_var}")

