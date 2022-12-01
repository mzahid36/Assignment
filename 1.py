# take input of two integer lists and Concatenate two lits index-wise

list1 = []
list2 = []
updatedList = []

n = int(input("Enter the range of these lists : ")) # user will input the range of these lists

for x in range(n):
    data1 = int(input("Enter integer value for list 1 : "))
    data2 = int(input("Enter integer value for list 2 : "))
    list1.append(data1)
    list2.append(data2)

    newData = list1[x] + list2[x] # adding values of two list index wise
    updatedList.append(newData)

print("Here is the list 1 : ",list1,"\nHere is the list 2 : ",list2)
print("Updated list after concatenated List 1 and List 2 : ",updatedList)
