num=[7,8,120,25,44,20,27]
print("Orginal list is: ",num)
num=[x for x in num if x%2!=0]
print("The list after removing even numbers: ",num)