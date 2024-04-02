#########################################################################################

# A first-class citizen (or object) in a programming language is an entity which supports
# all the operations generally available to other entities. Such as being passed as an argument,
# returned from a function, and assigned to a variable.

#########################################################################################
# Assigning Functions to Variables
def square(x):
    return (x * x)
print(square)           # Output: <function square at 0x000001A3F00FA340>
print(square.__name__)  # Output: square
print(type(square))     # Output: <class 'function'>

g = square(5)
print(g)                # Output: 25
print(type(g))          # Output: <class 'int'>

f = square
print(f)                # Output: <function square at 0x000001A3F00FA340>
print(type(f))          # Output: <class 'function'>
print(f(5))             # Output: 25


#########################################################################################
# Higher Order Functions

def cube(x):
    return x * x * x

def my_map(func, arg_list):         # my_map is a higher order function because it takes a function as an argument
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1, 2, 3, 4, 5])
print(squares)          # Output: [1, 4, 9, 16, 25]


#########################################################################################
# Returning Functions

def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message      # Como retornei log_message e não log_message(), log_message não é executado aqui.

log_hi = logger('Hi!')  
print()
print(log_hi)           # Output: <function logger.<locals>.log_message at 0x0000016EAD8DE340>
print(type(log_hi))     # Output: <class 'function'>
print(log_hi())         # Output: Log: Hi!
                        # Output: None -> Because log_message() does not return anything and it was executed by log_hi()
log_hi()                # Output: Log: Hi!



def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')      # Output: <h1>Test Headline!</h1>
print_h1('Another Headline!')   # Output: <h1>Another Headline!</h1>

print_p = html_tag('p')
print_p('Test Paragraph!')      # Output: <p>Test Paragraph!</p>










#pylint: disable-all

