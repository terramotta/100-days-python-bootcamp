from art import logo


def adicionar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


operacoes = {
    '+': adicionar,
    '-': subtrair,
    '*': multiplicar,
    '/': dividir,
}


def calculadora():
    print(logo)

    num1 = float(input("Qual é o primeiro número?: "))
    executar = True
    while executar:
        for e in operacoes:
            print(e)
        realizar = input("Digite uma operação matemática: ")
        num2 = float(input("Qual é o próximo número?: "))

        calculo = operacoes[realizar]
        resposta = calculo(num1, num2)

        print(f"{num1} {realizar} {num2} = {resposta}")
        print(f"Digite 's' para continuar calculando com {
              resposta}, digite 'n' para sair ou digite 'novo' para uma nova calculadora")
        continuar_calc = input("Digite s/n/novo: ")
        if continuar_calc == 's':
            executar = True
            num1 = resposta
        elif continuar_calc == 'n':
            executar = False
            print("\nAdeus.")
        elif continuar_calc == 'novo':
            calculadora()
        else:
            print("Resposta inválida.")
            executar = False
            print("\nAdeus.")


calculadora()
