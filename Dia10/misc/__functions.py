
def order_pizza(size: str, crust: str, *toppings: str, discount: float = 0.0, **order_details: str) -> dict:
    """
    Função para fazer um pedido de pizza.

    Argumentos:
    - size (str): Tamanho da pizza.
    - crust (str): Tipo de massa da pizza.
    - *toppings (tuple): Toppings adicionais da pizza.
    - discount (float): Desconto aplicado no pedido (valor padrão é 0.0).
    - **order_details (dict): Detalhes adicionais do pedido.

    Exemplo de uso:
    >>> order_pizza("grande", "fina", "pepperoni", "mushrooms", delivery=True, tip=5.00)
    Pedido de uma pizza grande com massa fina e os seguintes ingredientes:
    - pepperoni
    - mushrooms

    Detalhes do pedido:
    - delivery: True
    - tip: 5.0
    """
    print(f"Pedido de uma pizza {size} com massa {
          crust} e os seguintes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")

    print("\nDetalhes do pedido:")
    for key, value in order_details.items():
        print(f"- {key}: {value}")

    print(f"\nDesconto aplicado: {discount}")

    # Retornando um dicionário com os detalhes do pedido
    order_summary = {
        'size': size,
        'crust': crust,
        'toppings': toppings,
        'discount': discount,
        **order_details
    }

    return order_summary


print(order_pizza.__annotations__)
# {'size': <class 'str'>, 'crust': <class 'str'>, 'toppings': <class 'tuple'>, 'discount': <class 'float'>, '

print(order_pizza.__code__)
# <code object order_pizza at 0x00000220A706C390, file "c:\dev\python\Python_Bootcamp\Dia10_Functions\misc\__functions.py", line 1>

print(order_pizza.__defaults__)
# Isso retorna uma tupla com os valores padrão dos argumentos POSICIONAIS (antes de *)(Se aplicável) da função. Se não houver valores padrão, retorna None.

print(order_pizza.__kwdefaults__)
# {'discount': 0.0}

print(order_pizza.__name__)
# order_pizza

print(order_pizza.__module__)
# __functions

print(order_pizza.__doc__)
# Função para fazer um pedido de pizza.
#
#     Argumentos:
#     - size (str): Tamanho da pizza.
#     - crust (str): Tipo de massa da pizza.
#     - *toppings (tuple): Toppings adicionais da pizza.
#     - discount (float): Desconto aplicado no pedido (valor padrão é 0.0).
#     - **order_details (dict): Detalhes adicionais do pedido.
#
#     Exemplo de uso:
#     >>> order_pizza("grande", "fina", "pepperoni", "mushrooms", delivery=True, tip=5.00)
#     Pedido de uma pizza grande com massa fina e os seguintes ingredientes:
#     - pepperoni
#     - mushrooms
#
#     Detalhes do pedido:
#     - delivery: True
#     - tip: 5.0


# Retorna uma tupla com os nomes das variáveis locais e argumentos da função.
print(order_pizza.__code__.co_varnames)
# ('size', 'crust', 'toppings', 'discount', 'order_details', 'order_summary', 'topping', 'key', 'value')

# O número de argumentos esperados pela função.
print(order_pizza.__code__.co_argcount)
# 5

# O número de argumentos de palavra-chave somente (depois de *).
print(order_pizza.__code__.co_kwonlyargcount)
# 0

# O número de argumentos posicionais somente (antes de *).
print(order_pizza.__code__.co_posonlyargcount)
# 0

# O número de variáveis locais usadas pela função (incluindo argumentos).
print(order_pizza.__code__.co_nlocals)
# 9

# Significa que a função pode chamar outras funções aninhadas até 20 vezes.
print(order_pizza.__code__.co_stacksize)
# 20

print(order_pizza.__dict__)
# {}, because there are no attributes defined for the function.
