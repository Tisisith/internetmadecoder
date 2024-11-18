import string

print('''The password must meet the followig criteria:
      1. It must include at least 1 special character
      2. It must be at least 7 characters long
      3. It must include at least 1 number\n''')
while True:
    pw = input("Enter a password: ")
    number_of_char = 0
    number_of_num = 0
    number_of_spe =0
    total_number = len(pw)

    for x in pw:
        if x.isalpha():
            number_of_char+=1
        elif x.isdigit():
            number_of_num+=1
        elif x in string.punctuation:
            number_of_spe+=1

    if total_number >=12 and number_of_spe>=2 and number_of_num>=2:
        print("Your password is very strong")
    elif total_number >=7 and number_of_spe >=1 and number_of_num>=1:
        print("Your password is strong.")
    elif number_of_spe ==0:
        print("Please add a special character to your password")
    elif number_of_num ==0:
        print('Please add a number to your password.')
    else:
        print("Your password does not meet the criteria.")

    choice = input('Do you want to continue? y or n ')
    if choice == 'n':
        print("Goodbye")
        break





