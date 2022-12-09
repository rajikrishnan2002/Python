x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
z=int(input("enter the third number: "))
if (x>y)and(x>z):
    largest=x
elif (y>x)and(y>z):
    largest=y
else:
    largest=z
print("The largest number is",largest)