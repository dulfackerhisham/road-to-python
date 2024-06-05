# def main():
#     x = int(input("what's x? "))
#     print("x square is", square(x))


# def square(n):
#     return n * n

# main() 

# score = int(input("SCore: "))


# if score >=90:
#     print("A grade")
# elif score >= 80:
#     print("B grade")
# elif score >= 70:
#     print("C grade")
# elif score >= 60:
#     print("D grade")
# elif score >= 50:
#     print("E grade")
# else:
#     print("F grade")

# Loops ==>>>
#while loop =>
# i = 3       #1st case
# while i != 0:
#     print('hello dulfacker')
#     i = i - 1

# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# for loop
# for i in range(5):      #we can use _ instead of  a variable(i )
#     print("bark")

# small problems
# 1
# while True:
#     n = int(input("what's n "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Ssup")

# 2 (same problem with function)
# def main():
#     x = int(input("what's x "))
#     meow(x)

# def meow(to):
#     for _ in range(to):
#         print("meoooooowww")

# main()


# List
# students = ["Jack", "Rose", "Peter"]

# for q in range(len(students)):
#     print(q + 1, students[q])


# dictionary

# houseMem = {
#     "Hermione": "madakkara",
#     "harry": "ckv",
#     "dabu": "cheekka"
# }

# for peoples in houseMem:
#     print(peoples, houseMem[peoples])

students = [
    {"name": "hisham", "stream": "bcom", "year": 2019},
    {"name": "fatha", "stream": "bcm", "year": 2020},
    {"name": "ray", "stream": "bco", "year": 2024}
]

for stu in students:
    print(stu["name"], stu["stream"], stu["year"])