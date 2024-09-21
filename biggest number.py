x = (int(input("enter a number:")))
y = (int(input("enter a number:")))
z = (int(input("enter a number:")))

if (x > y and x > z):
    print(x, "is the biggest number from which you typed.")
elif (y > x and y > z):
    print(y, "is the biggest number from which you typed.")    
elif (z > x and z > y):
    print(z, "is the biggest number from which you typed.")    
else:
    print("Invalid")    