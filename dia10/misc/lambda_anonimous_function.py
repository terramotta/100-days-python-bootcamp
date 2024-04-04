students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']} house.")


# # O comportamento de ordenação do sorted() em relação ao tipo de retorno da função lambda (ou da função key) é fundamentalmente baseado nas propriedades naturais de ordenação desse tipo de dado. Aqui estão algumas possibilidades:

# String: Quando a função lambda retorna uma string, a ordenação é feita em ordem alfabética.
# Inteiro: Se a função lambda retorna um inteiro, a ordenação é feita em ordem crescente.
# Float: Para valores de ponto flutuante (floats), a ordenação é realizada em ordem crescente.
# Data: Se a função lambda retorna objetos de data, a ordenação é feita em ordem cronológica, ou seja, da data mais antiga para a mais recente.
# Objetos Personalizados: Se você estiver ordenando uma lista de objetos personalizados, a função lambda pode retornar qualquer tipo de dado, e a ordenação será baseada nas propriedades específicas que você definiu em sua classe.
# Tuplas: A função lambda pode retornar tuplas. Nesse caso, a ordenação será feita com base no primeiro elemento da tupla, e em caso de empate, no segundo elemento e assim por diante.
# Boleano: Se a função lambda retorna valores booleanos (True ou False), a ordenação será feita colocando os elementos False antes dos True.
# Listas: Se a função lambda retorna listas, a ordenação é feita com base no primeiro elemento da lista, e em caso de empate, no segundo elemento e assim por diante.

# Exemplo:
# import itertools
# lista = ['aa', 'bb', 'cc', 'dd']
# grupos = itertools.groupby(lista, key=lambda x: x[0])

# Nesse caso, estamos usando a função lambda para pegar o primeiro caracter de cada string da lista.


#pylint: disable-all