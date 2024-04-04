# pylint: disable=all

nome = f"Alice"
idade = 25
altura = 1.65

numero = f"{0.1:.10f}"

# Exemplo básico
mensagem = f"Olá, meu nome é {nome}!"
print(mensagem)

# Exemplo com expressões matemáticas
resultado = f"A soma de 2 e 3 é {2 + 3}."
print(resultado)

# Exemplo com formatação de números
pi = 3.14159
pi_formatado = f"O valor de pi é aproximadamente {pi:.4f}."
print(pi_formatado)

# Exemplo com expressões embutidas
preco = 29.99
desconto = 0.2
fstring = f"O preço final é {preco * (1 - desconto):.2f} reais."

# Exemplo com dicionários
data = {"nome": "Bob", "idade": 25}
fstring = f"Nome: {data['nome']}, Idade no próximo ano: {data['idade'] + 1}"