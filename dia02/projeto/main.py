print("\nBem-vindo à calculadora de gorjeta!")

valor_total = float(input("Qual é o valor total da conta?\nR$: "))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar?\nPercentual: "))
quantidade_pessoas = int(input("Quantas pessoas vão dividir a conta?\nPessoas: "))

total_por_pessoa = ("{:.2f}".format((((valor_total * (gorjeta / 100)) + valor_total) / quantidade_pessoas)))

print(f"Cada pessoa deve pagar: R${total_por_pessoa}", end='\n\n')

#pylint: disable-all
