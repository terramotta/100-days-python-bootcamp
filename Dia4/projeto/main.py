#pylint: disable-all
import random
import sys
import time

def main():
  # Strings que representam as escolhas
  pedra = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

  papel = '''
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  '''

  tesoura = '''
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  '''

  # Pergunta ao usuário e gera a escolha aleatória do computador
  escolha = input("\nO que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura\n0/1/2: ")
  escolha_computador = random.randint(0, 2)

  # Verifica se a entrada é um número válido
  if not escolha.isdigit():
      print("Você digitou um valor inválido, tente novamente e escolha um número entre 0-2.")
  else:
      escolha = int(escolha)
      # Verifica se a escolha está dentro do intervalo válido
      if escolha > 2:
          print("Você digitou um número inválido, tente novamente e escolha um número entre 0-2.")
      elif escolha == 0 or escolha == 1 or escolha == 2:
          # Mostra a escolha do jogador
          if escolha == 0:
              print(f"Você escolheu: Pedra {pedra}")
          elif escolha == 1:
              print(f"Você escolheu: Papel {papel}")
          elif escolha == 2:
              print(f"Você escolheu: Tesoura {tesoura}")

          # Mostra a escolha do computador
          if escolha_computador == 0:
              print(f"O computador escolheu: Pedra {pedra}")
              # Verifica o resultado do jogo
              if escolha == 2:
                  print("Você perdeu, Pedra vence contra Tesoura.")
              elif escolha == 0:
                  print("Empate!")
              else:
                  print("Você venceu!")

          elif escolha_computador == 1:
              print(f"O computador escolheu: Papel {papel}")
              # Verifica o resultado do jogo
              if escolha == 0:
                  print("Você perdeu, Papel vence contra Pedra.")
              elif escolha == 1:
                  print("Empate!")
              else:
                  print("Você venceu!")

          elif escolha_computador == 2:
              print(f"O computador escolheu: Tesoura {tesoura}")
              # Verifica o resultado do jogo
              if escolha == 1:
                  print("Você perdeu, Tesoura vence contra Papel.")
              elif escolha == 2:
                  print("Empate!")
              else:
                  print("Você venceu!")


main()
