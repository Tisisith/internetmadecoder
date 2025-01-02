print('''Welcome to Email Loop!

Choose your program:

1 - Cancellation Notice
2 - 14-day Notice
3 - 13-day Notice
4 - 12-day Notice
''')

letters = []
vehicles = []
collecting = True
program = int(input("What program? "))  # Corrected the input conversion to int

if program == 1 or program == 2 or program == 3 or program == 4:  # Check for valid program options

    while collecting:
        letter = input("Reference? ")
        if letter =='n':
            collecting = False
            continue

        vehicle = input("Vehicle? ")
        letters.append(letter)
        vehicles.append(vehicle)

    for i in range(len(letters)):
        if program == 1:
            print(f"\nStar Insurance Specialists - Cancellation Notice - {letters[i]} - {vehicles[i]}\n")
            print(f'''Hello,
    
Please see attached cancelation notice for non-payment of your insurance policy: {vehicles[i]}.
    
Kind regards,
    
$SYSTEMSIGNATURE$''')

        elif program == 2:
            print(f"\nStar Insurance - 14-Day Notice - {letters[i]} - {vehicles[i]}\n")
            print(f'''Dear Sir/Madam,

Please see attached 14-day notice for your insurance on your {vehicles[i]}.

If you are looking to continue this cover, please ensure the attached statement is addressed within this time.

Feel free to contact us on 0800 250 600 if you have any questions.

Thanks for letting us be part of your journey. Happy and safe travels.

The Accounts Team
''')

        elif program == 3:
            print(f"\nStar Insurance - 13-Day Notice - {letters[i]} - {vehicles[i]}\n")
            print(f'''Dear Sir/Madam,
            
Please see attached 13-day notice for your insurance on your {vehicles[i]}.

If you are looking to continue this cover, please ensure the attached statement is addressed within this time.

Feel free to contact us on 0800 250 600 if you have any questions.

Thanks for letting us be part of your journey. Happy and safe travels.

The Accounts Team
''')

        elif program == 4:
            print(f"\nStar Insurance - 12-Day Notice - {letters[i]} - {vehicles[i]}\n")
            print(f'''Dear Sir/Madam,
            
Please see attached 12-day notice for your insurance on your {vehicles[i]}.

If you are looking to continue this cover, please ensure the attached statement is addressed within this time.

Feel free to contact us on 0800 250 600 if you have any questions.

Thanks for letting us be part of your journey. Happy and safe travels.

The Accounts Team
''')
else:
    print("Invalid program option. Please choose from 1 to 4.")