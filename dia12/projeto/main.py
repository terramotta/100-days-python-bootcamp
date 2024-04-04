from art import logo
import random
from os import system


def guess_the_number():
    guess_this = random.randint(1, 100)
    print("Bem-vindo ao: ")
    print(logo)
    print("Estou pensando em um número entre 1 and 100, tente acertá-lo")
    difficulty = input(
        "Escolha a dificuldade, decida entr: 'facil' or 'dificil': ").strip().lower()
    if difficulty == 'facil':
        guesses = 10
    elif difficulty == 'dificil':
        guesses = 5

    while guesses > 0:
        if guesses > 1:
            print(f"Você tem {
                  guesses} tentativas restantes para adivinhar o número que estou pensando.")
        else:
            print(f"É sua última tentativa dessa vez.")
        attempt = int(input("Faça sua tentativa: "))
        if attempt > guess_this:
            print("Muito alto.")
        elif attempt < guess_this:
            print("Muito baixo.")
        if guesses == 1:
            print("Fim do jogo.")
        elif attempt == guess_this:
            def game_over():
                print(f"Correto! A resposta é {
                      guess_this}. Obrigado por jogar! 😁")
                return guesses - guesses
            guesses = game_over()
        guesses -= 1

    play_again = input(
        "\nVocê quer jogar novamente? Digite 'y' se sim e 'n' para sair.")
    if play_again == 'y':
        system('clear')
        guess_the_number()
    else:
        print("Adeus.")


guess_the_number()
