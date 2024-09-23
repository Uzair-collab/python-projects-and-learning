print("attendence needs to be of over 75%")
print("having medical causes can save you")

medical_cause = str(input("type \"Y\" for yes and \"N\" for no if you had medical causes:"))
attendence_check = int(input("what is your attendence percent?:"))


if (medical_cause == ("Y" or "y")):
    if (attendence_check >= 50):
        print("you can attend")
else:
    if (attendence_check >= 75):
        print("you can attend.")
    else:
        print("you can't attend.")