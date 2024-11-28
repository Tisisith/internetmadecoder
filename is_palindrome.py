
def is_palindrome(number):
    num = str(number)
    return num == num[::-1]

number = int(input("Give me a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome!")