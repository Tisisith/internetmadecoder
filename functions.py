def dollarizer(word):
    return word.replace('s','$')
def eurizer(word):
    return word.replace('e','€')
def replacer(c,d):
    new = c.replace('t',d[0])
    new1 = new.replace(d[0],d[1])
    return new1
def wonky_text(word):
    return eurizer(dollarizer(word))
def celsius_to_fahrenheit(celsius):
    h = (celsius * 9/5) +32
    return h
def age_in_days():
    age = int(input("Enter years of age " ))
    return age*365
def simple_interest(pa,ri,ty):
    si = pa*ri*ty
    return si
def plan_finances(pa,ri,ty,dfa):
    plan = pa*ri*ty
    if plan > dfa:
        return True
    else:
        return False
a = dollarizer('nelson')
print(a)
b = eurizer('nelson')
print(b)
c = input('Give me a word: ')
d = input('Give me 2 characters ')
e = replacer(c,d)
print(e)
f = wonky_text('etymologist')
print(f)
g = celsius_to_fahrenheit(90)
print(g)
print(age_in_days())
print(simple_interest(34,56,4))
print(plan_finances(500,0.12,1,600))


