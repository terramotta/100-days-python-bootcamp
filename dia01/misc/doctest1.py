#   Docstrings são comentários multi-linhas dentro de módulos, classes, etc.

# pylint: disable=missing-docstring

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> main()
7
>>> print('Hello, world!')
Hello, world!
"""

def main():
    a = 3
    b = 4
    result = a + b
    print(result)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("Todos os testes passaram com sucesso!")
