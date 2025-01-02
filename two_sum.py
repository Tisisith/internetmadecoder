
def two_sum(sum_list,target):
    for i in range(len(sum_list)):
        for x in range(i+1,len(sum_list)):
            if sum_list[i] + sum_list[x] == target:
                return [i,x]




lista = [0,1,2,3,4,5,6,7,8,9,10]

print(two_sum(lista,10))