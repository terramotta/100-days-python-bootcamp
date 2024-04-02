# https://www.youtube.com/watch?v=tKCURAMFdd4

# A basic function
def say_hello():
    return "Hello, world!"


# Decorator. Função que recebe uma func, adiciona funcionalidades e retorna outra func modificada.
def log_function(func):
    def wrapper():
        print(f"Running function: {func.__name__}")
        return func()
    return wrapper

# log_function é a função que será nosso decorator
# func é a função que será passada como argumento para o decorador
# wrapper é a função que será retornada pelo decorador


@log_function       # This means that log_function decorator is applied to say_hi function
def say_hi():
    return "Hi, world!"


# Above code is equivalent to
# say_hello = wrapper, pois log_function(say_hello) retorna wrapper sem executá-lo.
say_hello = log_function(say_hello)

##########################################################################################


def outer_function():
    message = 'Hi'

    def inner_function():       # inner_function is a closure, it has access to the variables in the outer_function
        print(message)

    return inner_function


my_func = outer_function()
print(type(my_func))    # <class 'function'>


# pylint: disable-all
