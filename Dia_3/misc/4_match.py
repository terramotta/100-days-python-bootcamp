name = input("Enter your name: ")

if name == Harry:
    print("Griffindor")
elif name == Ron:
    print("Griffindor")
elif name == Hermione:
    print("Griffindor")
elif name == Draco:
    print("Slytherin")
else:
    print("I don't know you")

######

if name == Harry or name == Ron or name == Hermione:
    print("Griffindor")
elif name == Draco:
    print("Slytherin")
else:
    print("I don't know you")

######

match name:
    case "Harry" | "Ron" | "Hermione":  # | é um operador de 'or'
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:                             # '_' é um wildcard, que significa "qualquer coisa"
        print("I don't know you")


match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

#pylint: disable-all