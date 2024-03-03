#pylint: disable=all

name = "Pedro Motta"
first, second = name.split()
print(f"{first} {second}")          # output: 'Pedro Motta'

# First Trick
n: int = 1000000
print(n) 
print(f'{n:_}')                     # output: '1_000_000'

# Second Trick
var: str = 'var'
print(f'{var:>20}')                 # output: '                 var'
print(f'{var:^20}')                 # output: '        var         '
print(f'{var:#>10}')                # output: '#######var'

# Third Trick
from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%y (%H:%M:%S)}') # output: '02.03.24 (10:06:39)'
print(f'{now:%c}')                  # output: 'Tue Mar  2 10:06:39 2024'

# Fourth Trick
n: float = 1234.7678
print(round(n, 2))                  # output:  1234.77
print(f'{n:.2f}')                   # output: '1234.77'

# Fifth Trick
a: int = 5
b: int = 10
my_var: str = 'Bob says hi'
print(f'a + b = {a + b}')           # output: 'a + b = 15'
print(f'{a + b = }')                # output: 'a + b = 15'
print(f'{my_var = }')               # output: "my_var = 'Bob says hi'"    

# Sixth Trick
a = 0.816562
print(f"{a:.4f}")                    # output: '0.8166' 
print(f"{a:.2%}")                    # output: '81.66%'




