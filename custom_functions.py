#numbers = (1,2,3,4,5,6,7,8,9,10 )

#def square(x):
#    return x*x

#new_list = list(map(square,numbers))
#print(new_list)

#for x in new_list:
#    if x % 2 ==0:
#        print(x)

#numbers = [100,200,300,400,500]

#new_list = list(map(lambda x: x*0.10,numbers))
#print(new_list)


#names = ['nelson','gymrat','house','jordan']

#new_names = list(map(str.upper,names))
#print(new_names)



#numbers = [1,2,3,4,5,6,7,8,9,10]

#a = list((map(lambda x: x*2,numbers)))
#print(a)

#MAX
x = [1,2,3,4,5]
def custom_max(x):
    for y in x:
        if y >y:
            y=y
    print(y)
custom_max(x)

#MIN
g = [90,890,78]
def custom_min(g):
    for y in g:
        if y < y:
            y=y
    print(y)
custom_min(g)


#LEN
string = ['jessa','tessa']
def custom_len(string):
    counte =0
    for x in string:
        counte +=1
    return counte
print(custom_len(string))

#Reverse
def custom_reversed(word):
    if isinstance(word, str):
        print(word[::-1])
    elif isinstance(word,list):
        for i in word:
            print(i[::-1])
    else:
        raise ValueError('Input must be a list or a string')

    
custom_reversed('gina')

#SORTED
def custom_sorted(data, reverse=True):
    # Check if the input is a string or a list
    if isinstance(data, str):
        is_string = True
        data = list(data)  # Convert string to a list of characters
    elif isinstance(data, list):
        is_string = False
    else:
        raise ValueError("Input must be a list or a string.")
    
    # Perform sorting using a basic algorithm (Bubble Sort)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (data[j] > data[j + 1] and not reverse) or (data[j] < data[j + 1] and reverse):
                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]
    
    # Convert back to string if the original input was a string
    if is_string:
        return ''.join(data)
    return data

print(custom_sorted("billa"))
    
        

