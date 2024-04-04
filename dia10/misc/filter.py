# Filter é similar a map. 
# A diferença é que o map aplica uma função a todos os itens da lista e retorna uma nova lista com os itens modificados,
# enquanto o filter retorna uma lista com os itens que retornam True para a função.

# Exemplo:
def starts_with_r(friend):
    return friend.startswith("R")

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]
start_with_r = filter(starts_with_r, friends)
print(*start_with_r, sep="\n")

# O código acima é equivalente a:
start_with_r = [friend for friend in friends if friend.startswith("R")]
print(*start_with_r, sep="\n")


#pylint: disable-all
