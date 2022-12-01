# Reverse a list in python (without reverse method)

mylist = [1, 2, 3, 4, 5]
revList = []    # empty list for storing reverse item.

for x in range(1,len(mylist)+1):
    revList.append(mylist[-x])

print(revList)
