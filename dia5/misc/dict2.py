students = [
    {"name": "Hermione", "house": "Griffindor", "Patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "Patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "Patronus": None}
]

for student in students:
#    print(student)          # {'name': 'Hermione', 'house': 'Griffindor', 'Patronus': 'Otter'}
#    print(type(student))    # <class 'dict'>
#    print(student["name"])  # Hermione

    print(student["name"], student["house"], student["Patronus"], sep = ", ")


# Dicionários são apenas um datatype que permite associar chaves a valores

#pylint: disable-all