n = int(input("number of rows: "))
num =1
for i in range (n):
    for j in range (i +1):
        print("{} ".format(num), end ='')
        num= num+1
    print()    