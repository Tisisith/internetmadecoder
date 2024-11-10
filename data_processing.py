a = input("Enter your sentence: ")
print(a.upper())
b = input("Input a paragraph: ")
words = b.split()
word_count = len(words)
print(f"The paragraph has {word_count} words")
c = input('Enter string or strings: ')
if c.isdigit():
    print(True)
else:
    print(False)

d = input('Enter a string: ').replace('a','o')
print(d)
e = input("Enter your full name: ")

g = e.split()
print("".join([h[0].capitalize() for h in g]))

f = input('Please enter one or more text')
print(f'The length of the string is {len(f)}')