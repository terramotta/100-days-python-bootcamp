# Description: Decorators are a design pattern in Python that allows a user to add new functionality to an existing object
# without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

# Decorators são funções que pegam outras funções como argumento, adicionam algum tipo
# de funcionalidade e então retornam outra função. Tudo isso sem alterar o source-code da função original.

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)     # decorator retorna o wrapper, que está esperando para ser executado.

# Ou seja, a variável decorated_display é do tipo class 'function', e não do tipo class 'NoneType'. 
# Ela aponta para a função wrapper_function que está esperando para ser executada e, quando for, irá apenas retornar
# a função original_function.

# type(decorated_display) -> <class 'function'>
# decorated_display() -> display function ran






##########################################################################################
# Decorar funções nos permite facilmente adicionar funcionalidades às nossas funções ao
# adicionar essas funcionalidades em nosso wrapper.

# Exemplo:








# pylint: disable-all