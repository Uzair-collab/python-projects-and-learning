unit_usage = int(input("enter unit usage:"))

if (unit_usage <= 50):
    print("your bill is: tk", (unit_usage*2.6)+25)
elif (unit_usage > 50 and unit_usage < 100):
    print("your bill is: tk", (unit_usage*3.25)+35)
elif (unit_usage > 100 and unit_usage < 200):
    print("your bill is: tk", (unit_usage*5.26)+45)
elif (unit_usage > 200):
    print("your bill is: tk", (unit_usage*8.45)+75)   
else:
    print("something is wrong")     