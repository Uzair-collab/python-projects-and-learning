word = (input("enter your word : "))
character = (input("enter your character : "))

i = 0
count = 0
while (i < len(word)):
    if ( word[i] == character):
        count = count + 1
    i = i+1
print(" no: of", character, "in", word, "is:", count)
