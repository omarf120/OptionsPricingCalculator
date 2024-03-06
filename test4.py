list1 = [1,2,3,4,5]
list2 = [0] * len(list1)
for x in range(len(list1)):
    list2[x] = list1[x] - 5
print(list1)
print(list2)