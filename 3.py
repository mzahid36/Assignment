# add a new item to the list after a specified item

li = ['C', 'C++', 'Java', 'Python']

n = input("Enter the item after which you want to add new item : ") # for integer item : int(input())
k = li.index(n) # looking for the index no. of the specified item.
data = input("Enter the new value : ")
li.insert(k+1, data) # adding new value after the specified item.

print(li)