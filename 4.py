# Remove all occurences of a specified item from a list

list1 = [5, 20, 15, 20, 25, 50, 20]

j = int(input("Enter a item to remove it from the list : "))

if j in list1:   # this condition will check for a correct list item. 
    x = list1.count(j)

    for k in range(x):
        list1.remove(j)
else:
    print("This item does not belong to this list. Please try with different value.")

print(list1)