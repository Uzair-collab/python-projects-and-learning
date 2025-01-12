def agify(name, age, message=", your age is"):
    return f"{name}{message} {age}"

infos = agify("Uzair", 12)

print(infos)