import time

def tictoc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nFuncion '{func.__name__}' executed. Elapsed time: {end-start}")
        return result
    return wrapper

@tictoc
def do_something():
    print('\nDoing something...')
    time.sleep(1)
    print('Done doing something.')


def do_something_else():
    print('\nDoing something else...')
    time.sleep(1)
    print('Done doing something else.')


print("\n Informações sobre a função do_something:")
print(f"Type(do_something) = {type(do_something)}")
print(f"do_something.__name__ = {do_something.__name__}")

print("")

print("\n Informações sobre a função do_something_else:")
print(f"Type(do_something_else) = {type(do_something_else)}")
print(f"do_something_else.__name__ = {do_something_else.__name__}")


do_something()
do_something_else()

print("\n\nEnd of script.")


#pylint: disable-all