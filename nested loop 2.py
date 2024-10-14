starting_number = (int(input("what is the starting no: ")))
ending_number = (int(input("what is the ending no: ")))

for number in range(starting_number, ending_number+1):
    if number > 1:
        for i in range(2, number):
            if(number % i == 0):
                break
        else:
            print(number)    


