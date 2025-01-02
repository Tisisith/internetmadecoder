#products = ['phone', 'tablet', 'laptop', 'journal']
#
#item = input('Enter product to search: ').lower()
#
#print(item in products)

#items = ['phone', 'tablet', 'map', 'glass']
#
#add_item = input('Enter product to add: ')
#
#add_after = input(f"After which item would you like to add {add_item} ")
#
#index = items.index(add_after)
#
#items.insert(index+1, add_item)
#
#print(items)

# products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}
#
# print(products)
# new_product = input("Enter a product you want to add: ")
# new_product_price = input("What is the price? ")
# products[new_product] = new_product_price
# print(f'The new products list is {products}')

#for x in range(5):
#    print("I love you, Camille!")

#fruits = ['apple','banana','orange']
#for x in fruits:
#    print(x)

#people = {"Camille":30, "Nelson":33,"Donna":32}
#for man in people.items():
#    print(man)

#counter = 1
#while counter<=10:
#    print(counter)
#    counter +=1

#counter =0
#while counter<=10:
#    print(counter)
#    if counter==5:
#        break
#    counter=counter+1
#print("Line after the loop")


#counter = 0
#while counter <=9:
#    counter += 1
#    if counter ==5:
#        continue
#   print(counter)

#cart=[]
#numbers = int(input('How many items do you want to include in the cart? '))
#items = 1
#while items<=numbers:
#    item = input('Enter an item into the cart ')
#    items += 1
#    cart.append(item)
#print(cart)

#cart=[]
#n = int(input('How many items? '))
#
#for x in range(n):
#    item= input("What item do you want to add into the cart: ")
#    cart.append(item)
#
#for y in cart:
#    print(y)

'''MY VERSION OF THE WHILE LOOP'''
# cart=[]
# y = input("Do you want to add an item in the cart? ")
# while y=='y'.lower():
#     item=input("What item do you want to add in the cart? ")
#     cart.append(item)
#     y1 = input("Do you want to add an item in the cart? ")
#     print(cart)
#     if y1=='n'.lower():
#         break
# print(f"Here are your items {cart}")

'''OTHER VERSION'''
#cart=[]
#while True:
#    choice = input("Do you want to add item to the cart? ")
#    if choice =='n'.lower():
#        break
#    item = input("What item do you want to add into the cart: ")
#    cart.append(item)
#print(f"Here are your items! {cart}")


products = [
    {'name':'iPhone','price':500000,'description':'a very expensive product'},
    {'name':'iPad','price':49879,'description':'a very nice tablet'},
    {'name':'travel','price':30000,'description':'stupid ideal'}
]
#ADDING ITEMS TO CART
#cart= []
#while True:
#    choice = input('Do you want to continue shopping?')
#    if choice=='y'.lower():
#        print("Here is the list of the products:\n")
#        for index, product in enumerate(products):
#            print(f"{index}: {product['name']}: {product['description']} : ${product['price']}\n")
#        product_id = int(input("What product ID would you like to purchase? "))
#        if products[product_id] in cart:
#            products[product_id]['quantity']+=1
#        else:
#            products[product_id]['quantity']=1
#            cart.append(products[product_id])
#        total = 0
#        print('Current contents are: ')
#        for product in cart:
#            print(f"{product['name']}: {product['price']}: QTY: {product['quantity']}")
#            total = total+ product['price']*product['quantity']
#            print(f'Your current total is {total}')
#    else:
#        break
#print(f"Thank you! Your total cart value is {total}")


#CODING CHALLENGES
#for x in range(5):
#    print('I am a programmer')
#
#def square():
#    for x in range(1,10):
#        print(x**2)
#square()

#def add(a,b):
#    print(a+b)
#
#add(4,5)


#def speed(distance, time):
#    print(distance/time)
#
#speed(distance=500,time=100)



#def area(radius, pi=3.14):
#    print(pi*radius*radius)
#
#area(50)

#def area(radius, pi=3.14):
#    print(pi*radius*radius)
#
#area(10,3.15)


#def area(radius,pi=3.14):
#    result = pi*radius*radius
#    return result
#
#def cost(circle_area,cost_per_sq_m):
#    tc = circle_area*cost_per_sq_m
#    return tc
#
#calculated_area = area(100)
#total_cost = cost(calculated_area, 10)
#
#print(total_cost)

#def area(r):
#    area = 3.14*r*r
#    circumference = 2 *3.14*r
#    return area, circumference
#
#a,c = area(100)
#print(f"Area is {a}, circumference is {c}")


#REMOVING DUPLICATES VERSION 1
#def remove_duplicates(numbers):
#    new_list=[]
#    for x in numbers:
#        if x not in new_list:
#            new_list.append(x)
#    return new_list
#
#ids = [1,2,3,4,5,6,7,1,3,4]
#a = remove_duplicates(ids)
#print(a)

#REMOVING DUPLICATES(SHORT VERSION)
#def remove_duplicates(numbers):
#    return list(set(numbers))
#
#ids = [1,2,3,4,1,2,4,5,6]
#result=remove_duplicates(ids)
#print(result)

# LOCAL VS GLOBAL VARIABLE

#CHECK IF A PALINDROME
#word = ('noon')
#l = len(word)
#
#palindrome_flag = True
#
#for x in range(l):
#    if word[x] != word[l-x-1]:
#        palindrome_flag=False
#        break
#    else:
#        palindrome_flag=True
#
#if palindrome_flag==True:
#    print('The word is a palindrome!')
#else:
#    print('The word is not a palindrome!')


#CHECK IF PALINDROME(FUNCTION VERSION)
#def check_palindrome(word):
#    l = len(word)
#    for x in range(l):
#        if word[x]!=word[l-x-1]:
#            return False
#    return True
#
#print(check_palindrome('racecar'))


#EMI Calculator
#def emi_calculator(principal, rate, time):
#    r = rate/12/100
#    emi = (principal * r*(1+r)**time)/ ((1+r)**time-1)
#    return emi
#
#print(emi_calculator(50000000,8.75,240))


#RECURSION
#def hello():
#    print("Hello")
#    hello()
#
#hello()

#FACTORIALS IN RECURSION
#def factorial(number):
#    if number ==1:
#        return 1
#    else:
#        return number * factorial(number-1)
#print(factorial(4))
#EXPLANATION
# factorial(4) => return 4 * factorial(3)
# factorial(3) => return 3 * factorial(2)
# factorial(2) => return 2 * factorial(1)

#MULTIPLE VARIABLES
#def add(*args):
#    sum=0
#    for n in args:
#        sum = sum+n
#    return sum
#print(add(1,2,3,4,5,9,23.56,20))

#MULTIPLE VARIABLES WITH KEYWORD ARGUMENTS
#def product(**kwargs):
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")
#
#product(name='iphone',product="700")
#product(name='iphone',price="400",description="an stupid idea")


#DECORATORS
#def chocolate():
#    print("Chocolate")
#
#def decorator(a):
#    def wrapper():
#        print('Wrapper inside up')
#        a()
#        print("Wrapper outside up")
#    return wrapper
#
#chocolate= (decorator(chocolate))
#chocolate()

#DECORATORS OTHER VERSION
#def decorator(a):
#    def wrapper():
#        print('Wrapper inside up')
#        a()
#        print("Wrapper outside up")
#    return wrapper
#@decorator
#def chocolate():
#    print("Chocolate")
#@decorator
#def cake():
#    print("Cake")
#chocolate()
#cake()

#DECORATORS WITH MULTIPLE ARGUMENTS
#def decorator(a):
#    def wrapper(*args,**kwargs):
#        print('Wrapper inside up')
#        a(*args,*kwargs)
#        print("Wrapper outside up")
#    return wrapper
#@decorator
#def chocolate():
#    print("Chocolate")
#@decorator
#def cake(name):
#    print(f"Cake "+ name)
#chocolate()
#cake('apple')


#DECORATOR THAT RETURNS A VALUE (MY VERSION)
#def summer_discount(func):
#    def wrapper(price):
#        b= func(price*0.20)
#        print(f"Our summer discount for your price is {b}")
#    return wrapper
#@summer_discount
#def total(price):
#    return price
#total(500)


#def summer_discount_decorator(func):
#    def wrapper(price):
#        func(price)
#        return func(price/2)
#    return wrapper
#
#@summer_discount_decorator
#def total(price):
#    return price
#
#print(total(1000))

#def bmi_calc(weight,height):
#    bmi = weight/(height**2)
#    return bmi
#
#weight = float(input("Enter your weight in kg "))
#height = float(input("Enter your height in meters "))
#
#print(bmi_calc(weight,height))

#MODULES
#import greet
#
#greet.hello()
#greet.bye()

#MODULES USING FROM
#from greet import hello, bye
#bye()

#RANDOM MODULE
#import random
#
#print(random.randint(1,10))

#DATETIME MODULE
#from datetime import date,datetime
#print(datetime.now())
#print(date.today())

#ERRORS & EXCEPTIONS
#SYNTAX ERROR - programming language error
#LOGICAL ERROR - program works but your program doesn't make sense/ output is not expected
#RUNTIME ERROR - error that happens when your program is actually running (Division by Zero, Undefined Variable errors)
#EXCEPTION HANDLING

#TRY/EXCEPT BLOCK

#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#result=0
#try:
#    result = n/m
#except ZeroDivisionError:
#    print("Cannot divide by zero!")
#print(result)

#ELSE BLOCK - happens when the exception didn't occur
#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#try:
#    result = n/m
#except ZeroDivisionError:
#    print("Cannot divide by zero!")
#else:
#    print(result)

#FINALLY BLOCK - happens no matter what
#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#try:
#    result = n/m
#except ZeroDivisionError:
#    print('cannot divide by zero!')
#else:
#    print(result)
#finally:
#    print("I love you!")

#CODING CHALLENGE:
#def divide(n,m):
#    result=n/m
#    return result
#try:
#    a= divide(56,56)
#except ZeroDivisionError:
#    print("cannot divide by zero!")
#else:
#    print(a)

#OPENING A FILE
#file = open('data.txt','r')
#content = file.readline()
#print(content)
#file.close()

#WRITING AND APPENDING FILE
#file = open('data.txt','a')
#content = "This is a third line"
#file.write(f"\n{content}")
#file.close()

#USING WITH IN OPENING FILES
#with open('data.txt','r') as file:
#    contents = file.read()
#    print(contents)


#with open('data.txt','r') as file:
#    line1 = file.readline()
#    print(line1)

#STRIP, LSTRIP, RSTRIP
#text = "    Hello World!   "
#stripped_text = text.strip()
#print(stripped_text)

#READLINE VS READLINES
#with open('data.txt','r') as file:
#    content = file.readlines()
#for line in content:
#    print(line.strip())


#READING AND WRITING FILES + Capitalize
#while True:
#    with open('write.txt','a') as file:
#        name = input("Enter a name: ")
#        file.write(name+"\n")
#        choice = input('Do you want to add another name: (y/n')
#        if choice == 'n':
#            break
#
#with open('write.txt','r') as file:
#    nelson = file.readlines()
#
#for x in nelson:
#    print(x.strip().capitalize()

#SAVING COMPLEX DATA
#def save_user_data():
#    with open('write.txt','a') as file:
#        name= input('Enter name: ')
#        email = input("Enter email: ")
#        contact = input('Enter contact: ')
#        user_data = f"Name: {name}\n Email: {email} \n Contact: {contact}\n"
#        file.write(user_data)
#
#def open_data():
#    with open('write.txt','r') as file:
#        print(file.read())
#
#save_user_data()
#open_data()

#SERIALIZING DATA USING JSON
#import json
#data = {
#    "name:":"Nelson",
#    "age:":30,
#    "city":"New York"
#}
#json_data = json.dumps(data)
#print(type(json_data))

#DESERIALIZATION
#import json
#json_data = '{"name":"John Doe","age":30,"city":"Philippines"}'
#data = json.loads(json_data)
#print(data['age'])

#LOADING AND ADDING NEW DATA (1 out of 4)
#import json
#import os
#def save_user_data():
#    user_list=[]
#    while True:
#        name = input("Enter name or type 'quit' ")
#        if name == 'quit':
#            break
#        age = input("Enter age : ")
#        location = input("Enter location: ")
#        user_dict = {
#            "name": name,
#            "age": age,
#            "location": location
#        }
#        user_list.append(user_dict)
#
#    if os.path.exists('new.json'):
#        with open('new.json','r') as file:
#            data = json.load(file)
#        user_list.extend(data)
#
#    with open('new.json','w') as file:
#        json.dump(user_list,file)
#
##READING EXISTING DATA + CRUD - CREATE READ UPDATE DELETE (2 out of 4)
#def read_user_data():
#
#    if not os.path.exists('new.json'):
#        print("No user data found")
#        return
#
#    with open('new.json','r') as file:
#        user_list = json.load(file)
#        for person in user_list:
#            print(f'Name:{person["name"]}')
#            print(f'Email:{person["age"]}')
#            print(f'location:{person["location"]}')
#            print('\n')
#
#
##UPDATING USER DATA (3 out of 4)
#def update_user_data(edit_name):
#
#    if not os.path.exists('new.json'):
#        print("No user data found")
#        return
#
#    with open('new.json','r') as file:
#        user_list = json.load(file)
#
#    user_found = False
#    for person in user_list:
#        if person['name'] == edit_name:
#            print('Data found for this person')
#            age = input('Input new age: ')
#            location = input('Input new location')
#            person["age"] = age
#            person["location"] = location
#            user_found = True
#            break
#
#
#    if not user_found:
#        print('Person does not exist')
#
#    with open('new.json','w') as file:
#        json.dump(user_list,file)
#    print("User data updated!")
#
##DELETING USER DATA
#def delete_user_data(delete_name):
#
#    if not os.path.exists('new.json'):
#        print("No user data found")
#        return
#
#    with open('new.json','r') as file:
#        user_list = json.load(file)
#
#    user_found = False
#    for person in user_list:
#        if person['name'] == delete_name:
#            user_list.remove(person)
#            user_found = True
#            break
#
#
#    if not user_found:
#        print('Person does not exist')
#
#    with open('new.json','w') as file:
#        json.dump(user_list,file)
#    print("User data updated!")
#
#delete_name = input("Whose data do you want to delete data for: ")
#delete_user_data(delete_name)

#LAMBDAS FUNCTION IN PYTHON
#result = (lambda x: x*2)(5)
#print(result)
#
#result = (lambda x,y: x+9)(5,9)
#print(result)

#GENERATORS
#def function():
#    counter = 0
#    while counter<=10:
#        yield counter
#        counter = counter + 1
#print(list(function()))
#
#def even_generator(x):
#    for i in range(x):
#        if i%2==0:
#            yield i
#
#print(list(even_generator(11)))
#

#CELSIUS TO FAHRENHEIT USING MAP

#celsius_temperatures = [25,30,15,10,35]
#
#print(list(map(lambda x: x*9/5 +32,celsius_temperatures)))


#EXTRACTING INITIALS FROM NAME
#names = ['John Doe', 'Alice Smith','Bob Ford']
#for x in names:
#    print(x.split()[0][0]+ x.split()[1][0])


#EXTRACTING INITIALS USING MAP
#NELSON'S WAY
#names = ['John Doe', 'Alice Smith','Bob Ford']
#a = list(map(lambda x: x.split()[0][0]+ x.split()[1][0],names))
#print(a)

#JOIN
#fruit=['a','p','p','l','e']
#print("".join(fruit))

#KAWAR'S WAY OF EXTRACTING INITIALS USING MAP
#names = ['John Doe', 'Alice Smith','Bob Ford']
#a = list(map(lambda name: "".join([n[0] for n in name.split()]),names))
#print(a)


#REVERSE A LIST USING A MAP
#word = 'abcdefghijklmno'
#print(word[::-1])

#words = ['Python', 'Java', 'Javascript', 'C++']
#a = list(map(lambda x: x[::-1],words))
#print(a)

#FIBONACCI SEQUENCE
#def fibonnaci(n):
#    if n<=0:
#        return []
#    elif n==1:
#        return [1]
#    elif n==2:
#        return [0,1]
#    else:
#        fib_sequence = [0,1]
#        fib_sequence.extend(map(lambda i: fib_sequence[i-1]+fib_sequence[i-2],range(2,n)))
#        return fib_sequence
#
#fibonnac = fibonnaci(100)
#print(fibonnac)


#FILTER PRIME NUMBERS
#numbers = [2,3,4,5,6,7,8,9]
#
#def is_prime(n):
#    if n<2:
#        return False
#    for i in range(2,n):
#        if n % i == 0:
#            return False
#    return True
#
#a = list(filter(is_prime,numbers))
#print(a)

#FILTERING STUDENTS
#students = [
#    {"name":"Alice","age":18,"grade":"A"},
#    {"name":"Bob","age":17,"grade":"B"},
#    {"name":"Charlie","age":19,"grade":"A"},
#    {"name":"David","age":16,"grade":"C"},
#    {"name":"Eve","age":21,"grade":"A"}
#]
#
#a= list(filter(lambda x: x['age']>=18 and x['grade']=="A", students))
#print(a)




#OBJECT ORIENTED PROGRAMMING (Class)
#class Product:
#    quantity = 200
#p1 = Product()
#print(p1.quantity)

#INSTANCE ATTRIBUTES
#class Product:
#    quantity =400
#
#    def __init__(self,name,price):  #not callable
#        self.name = name
#        self.price = price
#
#p1 = Product('iPhone',"500")
#p2 = Product('laptop', '900')
#
#print(p1.name)
#print(p1.price)
#print(p2.name)
#print(p2.price)


#METHODS IN OBJECT ORIENTED PROGRAMMING
#class Product:
#    quantity =400
#
#    def __init__(self,name,price):  #not callable
#        self.name = name
#        self.price = price
#
#    def summer_discount(self,discount_price):
#        self.price = self.price - self.price * discount_price/100
#
#p1 = Product('iPhone', 86300)
#p2 = Product('laptop',50000)
#
#p1.summer_discount(50)
#print(p1.price)
#p2.summer_discount(100)
#print(p2.price)

#FUNCTIONAL & OOP BASED WAY OF WRITING CODE
#class Product:
#    def __init__(self,name,price):
#        self.name = name
#        self.price = price
#
#    def get_data(self):
#        self.name = input("Enter the name of the product ")
#        self.price = input("Enter the name of the price ")
#
#    def put_data(self):
#        print(self.name)
#        print(self.price)
#
#p1 = Product("","")
#p1.get_data()
#p1.put_data()

#INHERITANCE
#class Product:
#    def __init__(self,name,price):
#        self.name = name
#        self.price = price
#
#    def get_data(self):
#        self.name = input("Enter the name of the product ")
#        self.price = input("Enter the name of the price ")
#
#    def put_data(self):
#        print(self.name)
#        print(self.price)
#
#class DigitalProduct(Product):
#    def __init__(self,link):
#        self.link = link
#
#    def get_link(self):
#        self.link = input("What is the link of the product")
#
#    def put_link(self):
#        print(self.link)
#
#
#p3 = DigitalProduct("")
#p3.get_data()
#p3.get_link()
#p3.put_data()
#p3.put_link()


#MULTIPLE INHERITANCE
#class A:
#    def method_a(self):
#        print('Method of A')
#
#class B:
#    def method_b(self):
#        print('Method of B')
#
#class C(A,B):
#    def method_c(self):
#        print('Method of C')
#
#cobject = C()
#cobject.method_a()
#cobject.method_b()
#cobject.method_c()

#MULTI-LEVEL INHERITANCE
#class A:
#    def method_a(self):
#        print('Method of A')
#
#class B(A):
#    def method_b(self):
#        print('Method of B')
#
#class C(B):
#    def method_c(self):
#        print('Method of C')
#
#cobject = C()
#cobject.method_a()
#cobject.method_b()
#cobject.method_c()

#POLYMORPHISM AND METHOD OVERRIDING

#class Food:
#    def type(self):
#        print('Food')
#
#class Fruit(Food):
#    def type(self):
#        print("Fruit")
#
#apple = Fruit()
#apple.type()

#Instance Method
#class Student:
#
#    def __init__(self,name):
#        self.name = name
#
#    def printed(self):
#        print(f'My name is {self.name}')
#
#    def length(self):
#        return len(self.name)
#
#a = Student('nelson')
#a.printed()
#b = Student('Mark')
#b.printed()
#c = a.length()
#print(c)
#d = b.length()
#print(d)
#
#Class Method
#class Student:
#    category = 'name'
#
#    def __init__(self,name):
#        self.name = name
#
#    def printed(self):
#        print(f'My name is {self.name}')
#
#    def length(self):
#        return len(self.name)
#
#    @classmethod #decorator
#    def info(cls):
#        print(f"The category is {cls.category}")
#
#
#a = Student('nelson')
#a.printed()
#b = Student('Mark')
#b.printed()
#c = a.length()
#print(c)
#d = b.length()
#print(d)
#Student.info() #this is the class instance

#STATIC METHOD

#class Student:
#    category = 'name'
#
#    def __init__(self,name):
#        self.name = name
#
#    def printed(self):
#        print(f'My name is {self.name}')
#
#    def length(self):
#        return len(self.name)
#
#    @classmethod #decorator
#    def info(cls):
#        print(f"The category is {cls.category}")
#
#    @staticmethod #static method are independent of class and inheritance method
#    def add(a,b):
#        return a+b
#
#
#a = Student('nelson')
#a.printed()
#b = Student('Mark')
#b.printed()
#c = a.length()
#print(c)
#d = b.length()
#print(d)
#Student.info() #this is the class instance
#print(Student.add(2,3)) #Static method


#NESTED CLASSES
#class Car:
#
#    def __init__(self,brand):
#        self.brand = brand
#        self.steering_object = self.Steering() #call the inner class
#
#    @staticmethod
#    def drive():
#        print("Drive")
#
#    class Steering:
#
#        @staticmethod
#        def rotate():
#            print("Rotate")
#
#car = Car("ABC")
#car.drive()
#
#steering = car.steering_object
#steering.rotate()


#NESTING CLASS EXAMPLE
#class Zoo:
#
#    def __init__(self):
#        self.animals =[]
#
#    def add_animal(self,name,species):
#        animal = self.Animal(name,species)
#        self.animals.append(animal)
#
#    class Animal:
#
#        def __init__(self,name,species):
#            self.name = name
#            self.species = species
#
#        def print_info(self):
#            print(f'Name: {self.name}, Species: {self.species}')
#
#zoo = Zoo()
#zoo.add_animal("Lion","Mammal")
#zoo.add_animal("Alligator","Reptile")
#
#for animal in zoo.animals:
#    animal.print_info()



#CONSTRUCTOR INHERITANCE
#class Parent:
#    def __init__(self): #Constructor
#        self.balance = 50000
#
#    def print_balance(self):
#        print(f'The balance is {self.balance}')
#
#class Child(Parent):
#    pass # no need to code if you're going to inherit the constructor
#
#nelson = Child()
#nelson.print_balance()


#OVERRIDING SUPERCLASS CONSTRUCTOR
#class Parent:
#    def __init__(self): #Constructor
#        self.balance = 50000
#
#    def print_balance(self):
#        print(f'The balance is {self.balance}')
#
#class Child(Parent):
#     def __init__(self):
#         self.balance=20000
#
#     def print_balance(self):
#         print(f'The balance is {self.balance}')
#
#
#nelson = Child()
#nelson.print_balance()

#USING SUPER
#class Parent:
#    def __init__(self): #Constructor
#        self.parent_balance = 50000
#
#    def display_balance(self): # Notice that both the superclass has the same method name
#        print(f'The balance is {self.parent_balance}')
#
#class Child(Parent):
#     def __init__(self):
#         super().__init__() #Accesses the constructor of the inherited class (Parent)
#         self.child_balance=20000
#
#     def display_balance(self): # Notice that both the superclass and the class who inherited has the same method name
#         print(f'The balance is {self.child_balance+self.parent_balance}')
#
#
#nelson = Child()
#nelson.display_balance()

#ENTIRE OOP EXAMPLE PART 1 (Every line has comments)
#Creating a class
#class Vehicle:
#    #Creating a constructor
#    def __init__(self,name,color):
#        #Instance variable
#        self.name=name
#        self.color=color
#
#    # Instance method
#    def display_info(self):
#        print(f'The car details are {self.name} and its color is {self.color}')
#    pass
#
##Inheritance
#class Car(Vehicle):
#    pass
#
##Create an object
#vehicle = Vehicle('nelson','blue')
#vehicle.display_info()
#
#car = Car("LuxuryCar","Black")
#car.display_info()
#

#STUDENT MANAGEMENT SYSTEM USING OOP
#class Student:
#    def __init__(self,name,age,roll_number):
#        self.name=name
#        self.age=age
#        self.roll_number=roll_number
#
#class School:
#    def __init__(self):
#        self.students=[]
#
#    def add_student(self,name,age,roll_number):
#        student = Student(name,age,roll_number)
#        self.students.append(student)
#
#    def print_info(self):
#        for student in self.students:
#            print(f'Name: {student.name}')
#            print(f'Age: {student.age}')
#            print(f'Roll Number: {student.roll_number}')
#            print("....................")
#
#
#name = input("Enter name of the student: ")
#age = input('Enter age: ')
#roll_number = input("What is the roll number? ")
#student = School()
#student.add_student(name,age,roll_number)
#student.print_info()

#CREATING A MENU
#class Student:
#    def __init__(self,name,age,roll_number):
#        self.name=name
#        self.age=age
#        self.roll_number=roll_number
#
#class School:
#    def __init__(self):
#        self.students=[]
#
#    def add_student(self,name,age,roll_number):
#        student = Student(name,age,roll_number)
#        self.students.append(student)
#
#    def print_info(self):
#        for student in self.students:
#            print(f'Name: {student.name}')
#            print(f'Age: {student.age}')
#            print(f'Roll Number: {student.roll_number}')
#            print("....................")
#
##EDITING INFO
#
#    def edit_info(self,option):
#        user_found = False
#        for student in self.students:
#            if option ==student.roll_number:
#                new_name=input("What is the new name of the student?")
#                new_age=input("What is the new age of the student?")
#                student.name=new_name
#                student.age=new_age
#                print('Info has been updated')
#                user_found = True
#
#        if not user_found:
#            print("There's nothing there")
#
##DELETING DATA
#    def delete_info(self,option):
#        user_found = False
#        for student in self.students:
#            if option == student.roll_number:
#                self.students.remove(student)
#                user_found = True
#                break
#        print(f"Roll number {student.roll_number} has been deleted")
#
#        if not user_found:
#            print('Person does not exist')
#
#
#student = School() #AN OBJECT
#while True:
#    choice = int(input("Enter your choice: \n 1) Add student  \n 2) Print list \n 3) Edit List \n "
#                       "4) Delete A Roll Number \n 5).Exit \n"))
#    if choice ==1:
#        name = input("Enter name of the student: ")
#        age = input('Enter age: ')
#        roll_number = input("What is the roll number? ")
#        student.add_student(name,age,roll_number)
#    elif choice ==2:
#        student.print_info()
#    elif choice ==3:
#        new_roll = input("What is the roll number? ")
#        student.edit_info(new_roll)
#    elif choice == 4:
#        del_option=input("Which roll number do you wish to delete? ")
#        student.delete_info(del_option)
#    elif choice==5:
#        print("Goodbye")
#        break
#    else:
#        print("Incorrect response. Try again")


        
#REGULAR EXPRESSIONS - a series of strings that contains patterns
#print(r"Hello \n World")  #r before the double quote will not read \n as an escape character - this is called a raw or pure string

#WRITING OUR FIRST REGULAR EXPRESSION
#import re
#string = "abc"
#pattern = "a"
#if re.match(pattern,string):
#    print("Match found")
#else:
#    print("No match found")

#MATCH VS. SEARCH
#import re
#string = "abc"
#pattern = "a"
#if re.search(pattern,string):
#    print("Match found")
#else:
#    print("No match found")

#META CHARACTERS
#STAR CHARACTER - ensures that the character preceding the asterisk or star is present 0 or more times in a pattern
#import re
#string = "abc"
#pattern = "ab*c"
#if re.match(pattern,string):
#    print("Match found") #This is match found
#else:
#    print("No match found")

#PLUS METACHARACTER   - ensures that the character preceding + must appear at least 1 time
#CURLY BRACES METACHARACTER - tells the computer to repeat the preceding character, as many number of times as the value inside the bracket
# repeating a character minimum of x times {x,}
#import re
#string = "abbbc"
#pattern = r"ab{3,}c"
#if re.match(pattern,string):
#    print("Match found") #This is match found
#else:
#    print("No match found")

#WILDCARD METACHARACTER
#Example 'a.b" means that we can place any character between a and b.

#Optional Metacharacter
#Example: "a-?b" This means that a - is optional, it may or may not be present

#CARET CHARACTER
#r"^91" anything that starts with the string following the ^

#CHARACTER CLASS
# r"[Pp]ython" - accepts both capital and lowercase p
# r"[a-z] - ranging, case sensitive
# r"[a-zA-Z]

#FIND ALL - checks all occurrences of a string in a given string
#import re
#text = "the sun is shining, the birds are singing"
#pattern = r"the"
#matches = re.findall(pattern,text)
#print(matches)

#CHARACTER CLASS AND FIND ALL- FINDING VOWELS
#import re
#text = "The cat and the dog sat out on the mat"
#pattern = r"[aeiou]"
#matches =re.findall(pattern,text)
#print(matches)

#SHORTHAND CHARACTER CLASSES
#import re
#text = "The meeting is scheduled at 9 AM"
#pattern=r"\d" # OR r"[0-9]"
#matches = re.findall(pattern,text)
#print(matches)
#
#r"\D" - returns all non-digit characters


# W SHORTHAND - returns all alphanumeric characters
# w - returns all alphanumeric characters, W - returns all non-alphanumeric characters
#import re
#text = "The variable name is my_var123"
#pattern = r"\S+"
#matches = re.findall(pattern,text)
#print(matches)

#S Shorthand - s -finding all spaces and tabs, S - returns all non-whitespace characters, S+ - combines all letters in a word together


#COMBINING SHORTHANDS AND METACHARACTERS - Find all strings with 1 or more occurrences of the letter "o"
#import re
#text = "Hellooooo, Python is awesomeeeeee!"
#pattern = r"\w*o+\w*" 
#matches = re.findall(pattern,text)
#print(matches)

#MATCHING PHONE NUMBERS PART 1 and 2
#import re
#text = "Please contact me at +1 (123) 456-7890 or via email at john@example.com"
#pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"
#matches = re.findall(pattern,text)
#print(matches)

#MATCHING EMAILS - NELSON'S VERSION
#import re
#text = "Please contact me at john@example.com or send a message to jane@example.com"
#pattern = r"\S+@.\S+"
#matches = re.findall(pattern,text)
#print(matches)

#CHECKING VALIDITY OF EMAILS
#import re
#text = "Please contact me at john@example.com or send a message to jane@example.com"
#pattern = r"\S+@.\S+"
#email = input("Enter email address: ")
#if re.match(pattern,email):
#    print("Valid email")
#else:
#    print("Invalid email")

#MATCHING DATES
#import re
#text = "Date: 2023-06-08, 1991-09-29"
#pattern = r"\d{4}-\d{2}-\d{2}"
#dates = re.findall(pattern,text)
#print(dates)

#TKINTER HELLO WORLD

#from tkinter import *
#root = Tk() #main tkinter window class
#root.geometry("300x300") # specifies how big the window is
#hello = Label(root,text="Hello World!") #creates a label for the window
#hello.pack() #actually shows the label on the window
#root.mainloop() #loops through the program so your windows shows

# UNDERSTANDING TKINTER WIDGETS
#from tkinter import *
#root = Tk()
#root.geometry("300x300")
#hello = Label(root,text="Hello World!",fg="blue",bg="white",font=("Verdana",24)) #widgets
#hello.pack()
#root.mainloop()

#BUTTON
#from tkinter import *
#
#def display():
#    print("Button clicked")
#
#root = Tk()
#root.geometry("300x300")
#button = Button(root,text="Click here",command=display)
#button.pack()
#root.mainloop()


from tkinter import *

#def display():
#    data = entry.get()
#    data2 = entry2.get()
#    print(f"{data} loves {data2}")
#
#root = Tk()
#root.geometry("300x300")
#entry = Entry(root)
#entry2 = Entry(root)
#entry.pack()
#entry2.pack()
#button = Button(root,text="Click here",command=display)
#button.pack()
#root.mainloop()

# ADDING TWO NUMBERS
#from tkinter import *
#
#def display():
#    data = int(entry.get())
#    data2 = int(entry2.get())
#    result = str(data + data2) #you need to convert the answer back to the string
#    answer.config(text="Answer is :"+result) #config lets you override what's on the existing label widget
#
#root = Tk()
#root.geometry("300x300")
#entry = Entry(root)
#entry2 = Entry(root)
#entry.pack()
#entry2.pack()
#button = Button(root,text="Click here",command=display)
#button.pack()
#answer = Label(root)
#answer.pack()
#root.mainloop()

#CHECKBOXES
#from tkinter import *
#def selected():
#    label.config(text=check_value.get())
#root = Tk()
#root.geometry("300x300")
#check_value = BooleanVar() #another TKinter class boolean
#checkbutton = Checkbutton(root,text="Accept terms",variable=check_value,command=selected)
#checkbutton.pack()
#label = Label(root)
#label.pack()
#root.mainloop()

#BEVERAGE SELECTOR
#from tkinter import *
#def selected():
#    sugar = sugar_var.get()
#    ice = ice_var.get()
#    cream = cream_var.get()
#    if sugar:
#        sugar = "With Sugar"
#    else:
#        sugar = "No sugar"
#    if ice:
#        ice = "With Ice"
#    else:
#        ice = "No Ice"
#    if cream:
#        cream = "With Cream"
#    else:
#        cream = "No Cream"
#    label.config(text="Options selected are: \n " +sugar+"\n" +ice +"\n"+cream)
#
#
#root = Tk()
#root.geometry("300x300")
#sugar_var = BooleanVar()
#ice_var = BooleanVar()
#cream_var = BooleanVar()
#sugar_check = Checkbutton(root,text="sugar",variable=sugar_var,command=selected)
#ice_check = Checkbutton(root,text="ice",variable=ice_var,command=selected)
#cream_check = Checkbutton(root,text="cream",variable=cream_var,command=selected)
#sugar_check.pack()
#ice_check.pack()
#cream_check.pack()
#label = Label(root)
#label.pack()
#root.mainloop()

#RADIOBUTTONS
#from tkinter import *
#def selected():
#    label.config(text="Choice of fuel is "+ fuel.get())
#root = Tk()
#root.geometry("300x300")
#fuel = StringVar(value="Petrol") # this is the default value when you first run the program
#radio1= Radiobutton(root,text="Petrol",variable=fuel,value="Petrol",command=selected) #variable= insures that you only choose 1 option for the radio options
#radio2= Radiobutton(root,text="Diesel",variable=fuel,value="Diesel",command=selected)
#radio3 = Radiobutton(root,text="Electric",variable=fuel,value="Electric",command=selected)
#radio1.pack()
#radio2.pack()
#radio3.pack()
#label = Label(root)
#label.pack()
#root.mainloop()

#FRAMES
#from tkinter import *
#
#root = Tk()
#root.geometry("300x300")
#frame= Frame(root)
#frame2 = Frame(root)
#frame.pack()
#frame2.pack(side=BOTTOM)
#button = Button(frame,text="Button1")
#button2 = Button(frame2,text="Button2")
#button.pack()
#button2.pack()
#
#root.mainloop()\

#ADDING PROPERTIES TO FRAMES
#from tkinter import *
#root = Tk()
#root.geometry("300x300")
#frame= Frame(root,highlightthickness=1,highlightbackground="Red",padx="20",pady="20")
#frame2 = Frame(root)
#frame.pack()
#frame2.pack(side=BOTTOM)
#button = Button(frame,text="Button1")
#button2 = Button(frame2,text="Button2")
#button.pack()
#button2.pack()
#root.mainloop()


#GRID LAYOUT MANAGER
#from tkinter import *
#root = Tk()
#label1 = Label(root,text="Email")
#label2 = Label(root,text="Password")
#text1 = Entry(root)
#text2 = Entry(root)
#label1.grid(row=0,column=0)
#text1.grid(row=0,column=1)
#label2.grid(row=1,column=0)
#text2.grid(row=1,column=1)
#button = Button(root,text="Login")
#button.grid(row=2,column=1)
#root.geometry("300x300")
#root.mainloop()

#CREATING A GRID
#from tkinter import *
#root = Tk()
#frame = Frame(root)
#for x in range(3):
#    for y in range(3):
#        frame = Frame(root)
#        frame.grid(row=x,column=y)
#        button = Button(frame,text=f'Row {x} \n Column {y}')
#        button.pack(pady=5,padx=5)
#root.mainloop()



#CREATING TKINTER APPS USING OOP

from tkinter import *
#class Demo:
#    def __init__(self,rootone):
#        frame = Frame(rootone)
#        frame.pack()
#
#        self.printbutton = Button(frame,text="Click here", command=self.printmessage)
#        self.printbutton.pack()
#
#        self.exitnow = Button(frame,text="Exit", command=frame.quit) # quit is a built-in function from Frame, no need to define
#        self.exitnow.pack()
#
#    def printmessage(self):
#        print("Button Clicked")
#
#root = Tk()
#b = Demo(root)
#root.mainloop()


#MENU
#from tkinter import *
#root = Tk()
#mymenu = Menu(root)
#
#def function1():
#    print("Project is here")
#
#def function2():
#    print("Project is saved")
#root.config(menu=mymenu)
#submenu = Menu(mymenu)
#submenu2 = Menu(mymenu)
#mymenu.add_cascade(label="File",menu=submenu)
#mymenu.add_cascade(label="Edit",menu=submenu2)
#submenu.add_command(label="Project",command=function1)
#submenu.add_command(label="Save",command=function2)
#root.mainloop()

#STATUS BAR
#from tkinter import *
#root = Tk()
#status = Label(root,text="This is the current status",bd=1,relief=SUNKEN,anchor="w") #bd = border, anchor = west, east, north and south
#status.pack(side=BOTTOM,fill=X)   #side = Where?, fill = fill entire row either X or Y
#root.mainloop()


#TOOLBAR

#from tkinter import *
#root = Tk()
#toolbar = Frame(root,bg="green")
#toolbar.pack()
#insertbutton =Button(toolbar,text="Insert File")
#deletebutton =Button(toolbar,text="Delete File")
#insertbutton.pack(side=LEFT,padx=2,pady=3)
#deletebutton.pack(side=LEFT,padx=2,pady=3)
#
#root.mainloop()


#MESSAGEBOX
#from tkinter import *
#import tkinter.messagebox
#root = Tk()
#tkinter.messagebox.showinfo("Title","This is a messagebox")
#response = tkinter.messagebox.askquestion("Question1","Do you like coffee")
#if response == "yes":
#    print("Here is a coffee for you")
#else:
#    print("Edi don't")
#root.mainloop()


#CALCULATOR APP USING TKINTER
#from tkinter import *
#import ast
#
#root = Tk()
#i=0
#def get_number(num):
#    global i # calling i as a global variable
#    entry.insert(i,num) # inserting the clicked button in the entry field
#    i+=1 # increments the placing of the next clicked button
#
#
#def get_operation(operator):
#    global i
#    length = len(operator)
#    entry.insert(i,operator)
#    i+=length #since our operator are not single spaced characters we ensure th
#
#def clear_all():
#    entry.delete(0,END) # deletes all characters on the field from index 0 until the End
#
#def calculate():
#    entire_string = entry.get()
#    try:
#        node = ast.parse(entire_string,mode="eval")
#        result = eval(compile(node,'<string>','eval'))
#        clear_all()
#        entry.insert(0,result)
#    except Exception:
#        clear_all()
#        entry.insert(0,'Error')
#
#def undo():
#    entire_string = entry.get()
#    if len(entire_string):
#        new_string = entire_string[:-1]
#        clear_all()
#        entry.insert(0,new_string)
#    else:
#        clear_all()
#        entry.insert(0,"")
#
#
#
#entry=Entry(root)
#entry.grid(row=1,columnspan=6)
#
#numbers=[1,2,3,4,5,6,7,8,9]
#counter = 0
#for x in range(3):
#    for y in range(3):
#        button_text = numbers[counter]
#        button = Button(root,text=button_text,width=2,height=2,command= lambda text=button_text:get_number(text))
#        button.grid(row=x+2,column=y)
#        counter += 1
#
#button = Button(root,text="0",width=2,height=2,command=lambda : get_number(0))
#button.grid(row=5,column=1) # placed at row 5 column 1
#
#count=0
#operations = ['+','-','*','/',"*3.14",'%','(','**',')',"**2"]
#for x in range(4):
#    for y in range(3): # 4 *3 = 12 but since we only have 10 operations on the list
#        if count<len(operations):
#            button = Button(root,text=operations[count],width=2,height=2,command=lambda text=operations[count]:get_operation(text))
#            count += 1
#            button.grid(row=x+2,column=y+3)
#
#Button(root,text="AC",width=2,height=2,command=clear_all).grid(row=5,column=0)
#Button(root,text="=",width=2,height=2,command=calculate).grid(row=5,column=2)
#Button(root,text="<-",width=2,height=2,command=lambda:undo()).grid(row=5,column=4)
#root.mainloop()


#REGULAR EXPRESSIONS REVISITED

#r"" - converts something to a pure string

#print(r"Hello \n world")

#import re #module for regular expression
#
#string = "bca"
#pattern = "a"
#if re.match("a", string): # if a is in the beginning of the string
#    print("match found")
#else:
#    print("match not found")
#
#match vs search - match look at the beginning of the string while search searches for the whole pattern



#META CHARACTERS  - special characters which don't match themselves. Instead they create some pattern which should be matched

#Examples - *,+,{...},.,?,^

# * makes sure that a particular character preceding it is present 0 or more times
#Example: pattern = "ab*c"
#Strings which match the pattern: ac, abc,abbc, abbbc

# + metacharacter means that the character preceding it must be present at least one time
#Example: pattern = ab+c
#matches: abc, abbc, abbbc
#not matches: ac

# {} - means that you want to repeat a particular character at least x times
#Example: pattern = "ab{2}"
#matches: abb, abbb, abbbb
#not matches: ab

# . states that the symbol can take place of any other symbol
#Example = "a.b" means that we can place any character between a and b.
#matches = acb, acbb
#not matches: ab, acab

# ? states any preceding character is optional between a string
#import re
#string = "pythonfile"
#pattern =r"pythonb?file"
#
#if re.match(pattern,string):
#    print("match found")
#else:
#    print("match not found")
#

# ^ - implies that it looks for a pattern that starts with a specific pattern
#import re
#string="8113483647364"
#pattern=r"^91"
#if re.match(pattern,string):
#    print("match found")
#else:
#    print("match not found")


#CHARACTER CLASSES PART 1
#import re
#string="1233A"
#pattern=r"\d{4}" # \d ensures that we're only looking for digits and {5} indicates that at least we're looking for 5 digits
#if re.match(pattern,string):
#    print('Match found')
#else:
#    print("No match found")
#
#\D - looks for non digit characters
#\w - matches for alphanumeric = letters and numbers


#CHARACTER CLASSES PART 2
#import re
#string="zython"
#pattern=r"^[a-zA-Z]ython"  #[] - indicates that we're looking for a specific class of characters. In this case p or P
#if re.match(pattern,string):
#    print("Match found")
#else:
#    print("No match found")

#[a-zA-Z] indicates that you want to accept any either lower case or uppercase letters in a pattern


#WRITING CLEAN PYTHON CODE BEST PRACTICES
#1. IT IS READABLE AND USEFUL FOR COLLABORATION, VARIABLES AND FUNCTION NAMES ARE TOP-NOTCH
#2. USE COMMENTS WHEN NECESSARY
#3. USE SPACES RATHER THAN TABS FOR INDENTATION
#4. USE 79 CHARACTERS BELOW FOR EACH LINE OF CODE
#5. USE 2 BLANK LINES FOR EVERY SUCCEEDING FUNCTION
#6. FOR CLASS METHODS, USE 1 BLANK LINE FOR EACH METHOD
#7. LEAVE ONE SPACE FROM VARIABLE TO ITS CONTENT. x = y
#8. FOR KEYWORD ARGUMENTS DON'T USE SPACES, write(message="hello")
#9. WHILE USING CLASSES, USE CamelCase Conventions, class NewStudents:
#10. FOR FUNCTIONS, USE SMALLCASE LETTERS, calculate_total():
#11. IMPORT STATEMENTS SHOULD ALWAYS BE ON THE TOP OF YOUR FILE
#12. ALWAYS INDICATE THE NAME OF THE PACKAGE AND THE MODULE YOU'RE GOING TO USE, from x import y
#13. ALWAYS MAKE SURE THAT YOU ALWAYS CHECK FOR A CONDITION e.g if a file or variable is empty,
#14. USE LIST COMPREHENSIIONS WHENEVER POSSIBLE INSTEAD OF MAP AND LAMBDAS
#15. USE AN ELSE BLOCK FOR FOR LOOPS IF NECESSARY

#a = [1,2,3,4,5,6,7,8]
#result = [x*2 for x in a]
#print(result)

#for x in range(5):
#    print(x)
#    if x == 4:
#        break
#else:
#    print("This is the else block")






