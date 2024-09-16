amount = (int(input("Enter the amount of money that you want to withdraw : ")))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("number of 100 taka notes", note_1)
print("number of 50 taka notes", note_2)
print("number of 10 taka notes", note_3)