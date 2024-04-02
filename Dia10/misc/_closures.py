# Closures
# A closure is a function object that has access to variables in its
# enclosing scope, even if the variables are no longer in scope.

# Therefore, in simple terms: A closure is an inner function that remembers and has access
# to variables in the local scope in which it was created even after the outer function has finished executing"

# Let's start with an example:

# logging module is used to log messages to the console.
import logging


def outer_func1():
    message = "Hi"

    def inner_func1():
        # free variable, because it is not defined in inner_func() but it is accessible.
        print(message)

    return inner_func1()

# outer_func1()            # Output: Hi


##########################################################################################

# Exemplo 1:

def outer_func():
    message = "Hi"

    def inner_func():
        # free variable, because it is not defined in inner_func() but it is accessible.
        print(message)

    # # I'm returning the inner function, but not executing it, because it does not have ().
    return inner_func


# my_func variable is now a function object that points to the inner_func() function.
my_func = outer_func()
# Output: <function outer_func.<locals>.inner_func at 0x0000021D3D3D3D30>
print(my_func)
print(my_func.__name__)         # Output: inner_func

my_func()                       # Output: Hi
my_func()                       # Output: Hi
my_func()                       # Output: Hi

# O detalhe aqui é que a variável message está sendo lembrada, ou seja, a função interna está
# lembrando do valor da variável message mesmo após a função externa ter terminado de executar.

# Na prática, essa é a definição de um closure, uma função interna que lembra de variáveis
# do escopo local onde ela foi criada, mesmo após a função externa ter terminado de executar.

# Na prática, o valor da variável está sendo armazenado em um espaço de memória que a função interna
# tem acesso, mesmo após a função externa ter terminado de executar.

# Esse espaço de memória só é liberado quando a função interna não é mais referenciada por nenhuma variável.
# Quem cuida dissos é o garbage collector do Python.


##########################################################################################

# Exemplo 2:

def outer_func2(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func2("Hi")
hello_func = outer_func2("Hello")

hi_func()                       # Output: Hi
hello_func()                    # Output: Hello

# Percebemos que cada função interna tem acesso a uma variável message diferente, pois
# cada uma foi criada em um escopo diferente.

# "A closure closes over the free variables from their environment."

##########################################################################################

# Exemplo 3:

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    # *args is used to pass a variable number of arguments to a function.
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# logger() function returns a function object that points to log_func() function.
add_logger = logger(add)
sub_logger = logger(sub)


add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

# example.log:
# INFO:root:Running "add" with arguments (3, 3)
# INFO:root:Running "add" with arguments (4, 5)
# INFO:root:Running "sub" with arguments (10, 5)
# INFO:root:Running "sub" with arguments (20, 10)


# pylint: disable-all
