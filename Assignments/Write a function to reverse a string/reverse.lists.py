def main():
    name = input("enter your name ")
    print("reversed string:", reverse_str(name))

def reverse_str(name):
    return name[::-1]

main()