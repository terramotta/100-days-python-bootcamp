import random

def main():
    print("Bem vindo ao gerador de senhas!")
    simbolos = get_int("Quantos símbolos você quer em sua senha? ")
    numeros  = get_int("Quantos números você quer em sua senha? ")
    letras   = get_int("Quantas letras você quer em sua senha? ")
    senha = gerar_senha(simbolos, numeros, letras)
    print(f"Aqui está sua senha: {senha}")

def get_int(prompt):
    while True:
        try:
            numero = int(input(prompt))
        except(ValueError, EOFError, TypeError):            # Importante a sintaxe de except()
            print("Por favor, insira um número válido.")
            continue

        if numero <= 0:
            print("Por favor, insira um número maior que zero.")
        else:
            return numero


def gerar_senha(numero_de_simbolos, numero_de_numeros, numero_de_letras):
    senha = ""      # string vazia no momento
    simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';',
                '"', "'", '<', '>', ',', '.', '?', '/']
    numeros  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letras   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']

    tamanho_senha = numero_de_simbolos + numero_de_numeros + numero_de_letras
    possiveis_opcoes_de_caracter = ['simbolo', 'numero', 'letra']

    while tamanho_senha > len(senha):
        for _ in range(tamanho_senha):
            tipo_de_caracter_escolhido   = random.choice(possiveis_opcoes_de_caracter)

            if (tipo_de_caracter_escolhido   == 'simbolo' and numero_de_simbolos > 0):
                senha = senha + str(random.choice(simbolos))
                numero_de_simbolos = numero_de_simbolos - 1

            elif (tipo_de_caracter_escolhido   == 'numero' and numero_de_numeros > 0):
                senha = senha + str(random.choice(numeros))
                numero_de_numeros = numero_de_numeros - 1

            elif (tipo_de_caracter_escolhido   == 'letra' and numero_de_letras > 0):
                senha = senha + str(random.choice(letras))
                numero_de_letras = numero_de_letras - 1

    return senha

main()



#pylint: disable-all
