# Variables and their types in Python

# Integer variable
age = 25
type(age)           # Output: int

# Floating-point variable
height = 6/4
type(height)        # Output: float

# String variable
name = "John Doe"
type(name)          # Output: str
name[2]             # Output: h

character = 'a'
type(character)     # Output: str (not char)

# Boolean variable
is_student = True 
type(is_student)    # Output: bool

# List variable, lembra um array em outras linguagens de programação, mas é mais flexível e pode conter diferentes tipos de dados.
fruits = ["apple", "banana", "cherry"]

# Tuple variable, lembra uma lista, mas é imutável
colors = ("red", "green", "blue")

# Dictionary variable, lembra JSON
person = {"name": "John", "age": 25, "is_student": True}

# Set variable, lembra uma lista, mas não pode conter elementos duplicados.
unique_numbers = {1, 2, 3, 4, 5}

# None variable, é um tipo de dado que representa a ausência de valor. Em termos de eficiência de memória, None é mais eficiente do que usar uma string vazia ou zero.
nothing = None


# pylint: disable=all