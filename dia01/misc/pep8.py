# pylint: disable-all
# https://peps.python.org/pep-0008/

# Importações devem ser feitas em linhas separadas
import os
import sys

# Constantes devem ser escritas em letras maiúsculas com sublinhados
CONSTANTE_EXEMPLO = 10

# Funções devem ser escritas em letras minúsculas com sublinhados
def funcao_exemplo(argumento1, argumento2):
    # Variáveis devem ser escritas em letras minúsculas com sublinhados
    variavel_exemplo = argumento1 + argumento2

    # Evite linhas com mais de 79 caracteres
    resultado = variavel_exemplo * CONSTANTE_EXEMPLO

    # Use espaços em branco para separar operadores e após vírgulas
    if resultado > 100:
        print("O resultado é maior que 100.")
    else:
        print("O resultado é menor ou igual a 100.")

    # Use 4 espaços para indentação
    for i in range(5):
        # Evite espaços em branco no final das linhas
        print(i)

    # Evite linhas em branco extras
    return resultado

# Chame a função principal
funcao_exemplo(5, 10)



