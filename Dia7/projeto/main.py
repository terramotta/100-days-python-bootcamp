import requests
import json
import os
from hangman_art import logo2, logo3

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_palavra_randomica():
    # Usar uma API para buscar um json com uma palavra randômica
    response = requests.get("https://random-word-api.herokuapp.com/word")

    # Usar a biblioteca json para transformar o json em um dicionário e então retorná-lo    
    return response.json()[0]

def atualiza_desenho(vidas):
    desenhos = [
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """
    ]
    print(desenhos[vidas])

def gerar_espaços_branco(tamanho_palavra):
    lista_de_caracteres = []
    espaço_em_branco = '_'
    for i in range(tamanho_palavra):
        lista_de_caracteres.append(espaço_em_branco)
    return lista_de_caracteres

def get_input(prompt):
    while True:
        try:
            while True:
                user_input = input(prompt)
                if user_input.isalpha() and len(user_input) == 1:
                    limpar_tela()
                    break
                else:
                    print('Digite apenas uma letra')
            return user_input
        except ValueError or TypeError:
            print('Digite uma letra')

def tentativa_usuario(palavra_randomica, vidas):
    # Pede para o usuário uma letra
    input_usuario = get_input('Digite uma letra: ')
    if input_usuario in palavra_randomica:
        return 'Acertou', input_usuario
    else:
        return 'Errou', input_usuario

def atualiza_lista_de_caracteres(lista_de_caracteres, letra, palavra):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            lista_de_caracteres[i] = letra
    return lista_de_caracteres

def main():
    vidas = 6
    acertos = 0

    # Mensagem de boas vindas
    limpar_tela()
    print(logo3)
    print("\nBem vindo ao jogo da Forca.\n")
    
    # Gerar palavra randômica
    palavra_randomica  = gerar_palavra_randomica().lower()

    # Inicializando a lista de caracteres com espaços em branco
    lista_de_caracteres = gerar_espaços_branco(len(palavra_randomica))
    print(palavra_randomica)

    # Diminui vida ou aumenta acertos
    while (vidas > 0 and acertos < len(palavra_randomica)):

        for elemento in lista_de_caracteres:
            print(elemento, end=' ')         # '_' '_' '_' '_' '_' '_' '_'
        print('\n')
        resultado_tentativa, input_usuario = tentativa_usuario(palavra_randomica, vidas)

        match resultado_tentativa:
            case 'Errou':
                vidas -= 1
                print(f'Você errou, e ainda tem {vidas} vidas')
                atualiza_desenho(vidas)
            case 'Acertou':
                print('Você acertou')
                acertos += 1
                atualiza_lista_de_caracteres(lista_de_caracteres, input_usuario, palavra_randomica)
    
    if acertos == len(palavra_randomica):
        print('Você venceu')
        print(logo2)
    elif vidas == 0:
        print('Você perdeu')

    









#pylint: disable-all

if __name__ == "__main__":
    main()