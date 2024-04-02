def main():
    yell("This", "is", "CS50!")     # 3 argumentos

def yell(*words):
    upper_cased = map(str.upper, words)
    print(*upper_cased)


if __name__ == "__main__":
    main()

# map é uma função que aplica uma função a cada item de um iterável (lista, tupla, etc) e retorna um iterador
# map(função, iterável).
# Flerta com o conceito de programação funcional.
# print(type(upper_cased))        # <class 'map'>


#pylint: disable-all