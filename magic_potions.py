potions = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"] }

print('''Welcome to the Magic Potion Shop!
      Here are the potions we offer:
      Invisibility Potion
      Flying Potion
      Healing Potion''')
stop_shopping = "You chose to stop shopping."
potion = input("Which potion would you like to buy ingredients for? ")

if potion in potions:
    print(f'\nThe ingredients for {potion} are: ')
    for x in potions[potion]:
        print(x)

    print("Let's start buying the ingredients!")
    while True:
        q1 = input(f'Do you want to buy {potions[potion][0]} (yes/no) ')
        if q1 == 'no':
            print(stop_shopping)
            break
        else:
            print(f'You bought {potions[potion][0]}! ')
            q2= input(f'Do you want to buy {potions[potion][1]} (yes/no) ')
            if q2 == 'no':
                print(stop_shopping)
                break
            else:
                print(f'You bought {potions[potion][1]}! ')
                q3 = input(f'Do you want to buy {potions[potion][2]} (yes/no) ')
                if q3 == 'no':
                    print(stop_shopping)
                    break
                else:
                    print(f'You bought {potions[potion][1]}! \n')
                    print(f'Congratulations! You bought all the ingredients for {potion}!')
                    break
            

else:
    print("That's none of the potions !")