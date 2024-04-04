# pylint: disable-all

# forma com while, correta mas demorada
i = 0
while i < 10:
    print("meow")
    i += 1

# forma menos mecânica
for _ in range(10):     # range(10) não é uma lista, é um iterável, que é uma lista preguiçosa
    print("meow")       # range(start, stop[, step])
# A forma que for funciona é, ele inicializa a variável que eu mandei criar,
# e a cada iteração ele a iguá-la a um elemento do iterável, até que o iterável ou lista acabe.

#####################

while True:             # loop infinito
    number = int(input("Give me a number: "))
    if (number <= 0):
        continue
    else:
        break
print("meow\n" * number, end="")


# Forma mais correta
while True:             # loop infinito
    number = int(input("Give me a number: "))
    if number > 0:
        break
print("meow\n" * number, end="")
