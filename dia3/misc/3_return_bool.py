# Is a given number even or odd

def main():
    x = int(input("Enter a number: "))
    if is_even(x):                # if is_even(x) returns 'True' or any non-zero value
        print("Even")

def is_even(number):
    return (number % 2 == 0)    # This is the most recommended way to return a boolean value
                                # O símbolo == indica que esse resultado será type 'bool'








#pylint: disable-all