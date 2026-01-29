text = input("Enter a string: ")
char_count ={}
for char in text:
    if char in char_count:
        char_count[char]+= 1
    else:
        char_count[char]= 1
print("Character frequencies: ")
for char, count in char_count.items():
    print(f"{char}: {count}")