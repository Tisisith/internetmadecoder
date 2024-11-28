def remove_element(lista,number):
    result_list=[]
    for a in lista:
        if a ==number:
            continue
        else:
            result_list.append(a)
    return result_list

print(remove_element([4,5,7,8,9,3,2,1,6,4,3,2,4,7],4))