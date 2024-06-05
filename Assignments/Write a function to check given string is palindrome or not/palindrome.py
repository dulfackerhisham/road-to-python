value = input("enter a palindrome or normal text ")

# value_re is a type of reversed iterator so we convert that to empty string
value_re = "".join(reversed(value))

if value == value_re:
    print(f"{value} is palindrome")
else:
    print(f"{value} is not palindrome")