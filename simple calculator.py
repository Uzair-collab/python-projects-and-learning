num1 = int(input("enter first number:"))
operater = (input("enter the operater that you want to operate with:"))
num2 = int(input("enter second number:"))

if (operater == "+"):
    print(num1 + num2)
elif (operater == "-"):
    print(num1 - num2) 
elif (operater == "x"):
    print(num1 * num2)
elif (operater == "/"):
    print(num1 / num2) 
else :
    print("no operater")        