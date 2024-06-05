vowels =("a", "e", "i", "o", "u")
text = input("enter a text ").lower()
count = 0

for i in text:
    if i in vowels:
        count += 1

if count == 0:
    print(f"there are no vowels present in {text}")
else:
    print(f"there are {count} vowels in {text}")