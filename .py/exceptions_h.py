# try:
#     num = int(input("enter an integer "))
#     b = [8, 6, 7, 55, 93]
#     print(b[num])
# except ValueError:
#     print("entered number is not an integer")
# except IndexError:
#     print("Index error")

'''FINALLY'''
def functu():
    try:
        a = [1,6,5,7]
        i = int(input("enter the index"))
        return a[i]
    except IndexError:
        print("some error occured")
    finally:
        print("im always executed")

print(functu())