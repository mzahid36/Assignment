# add a new item to the list after a specified item

li = ['C', 'C++', 'Java', 'Python']

n = input("Enter the item after which you want to add new item : ")
k = li.index(n)
data = input("Enter the new value : ")
li.insert(k+1, data)

print(li)