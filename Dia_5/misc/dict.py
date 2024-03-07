# students = ['Harry', 'Ron', 'Hermione', 'Draco']
# houses = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]

# Dicionários me deixam usar strings como índices, index.abs
# Diferente das listas, que só aceitam inteiros

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
    }

for student in students:
    # print(student)                                # Imprime só as chaves. Poderia ser as casas, mas não é o caso no Python
    print(student, students[student], sep = ", ")   # Imprime só os valores

# Output = Hermione, Griffindor
#          Harry, Griffindor
#          Ron, Griffindor
#          Draco, Slytherin

#pylint: disable-all