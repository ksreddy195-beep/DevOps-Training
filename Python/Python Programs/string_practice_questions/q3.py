text = input("Enter a string of your choice")

reversed_text = text[::-1]

if text == reversed_text:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")