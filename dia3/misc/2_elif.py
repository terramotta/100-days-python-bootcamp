score = int(input("What's your score? "))

# Método 1, menos eficiente
if score >= 90 and score >= 100:
    print("You got an A")
elif score >= 80 and score < 90:
    print("You got a B")
elif score >= 70 and score < 80:
    print("You got a C")
elif score >= 60 and score < 70:
    print("You got a D")
else:
    print("You got an F")

####-####-####

# Método 2, mais eficiente
if   90 >= score >= 100:
    print("You got an A")
elif 80 <= score < 90:
    print("You got a B")
elif 70 <= score < 80:
    print("You got a C")
elif 60 <= score < 70:
    print("You got a D")
else:
    print("You got an F")

####-####-####

# Método 3, mais eficiente
if   score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got an F")




#pylint: disable-all