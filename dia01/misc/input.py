#input(prompt='', /)
#    Lê uma string da entrada padrão. A quebra de linha final é removida.
#
#    A string de prompt, se fornecida, é impressa na saída padrão sem uma
#    quebra de linha final antes de ler a entrada.
#
#    Se o usuário atingir o EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), levanta EOFError.
#    Em sistemas *nix, o readline é usado se estiver disponível.

# Em Python, o / na assinatura da função indica que todos os parâmetros antes dele são apenas posicionais,
# o que significa que eles devem ser passados na ordem em que são definidos na função e não podem ser passados
# como argumentos de palavras-chave.

# Exemplo 1: Lendo uma string da entrada padrão
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Exemplo 2: Lendo um número inteiro da entrada padrão
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

# O que input() faz é literalmente trocar seu valor pela string que o usuário digitar.
# Um bom local para ver isso na prática é no Thonny IDE. Lá, você pode ver o valor de uma variável em tempo real.

# pylint: disable=all