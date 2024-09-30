x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))
z = int(input("Enter value for z:"))
lst =[x,y,z]
lst.sort()
x,y,z = lst[0],lst[1],lst[2]
print("value of x after swapping:",x)
print("value of y after swapping:",y)
print("value of z after swapping:",z)