import time

def time_performance(func):
    def wrapper():      # wrapper em português é embrulho, que é o que o decorator faz
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} ran in "\
              f"{end - start:.9f} seconds.")
    return wrapper      # retorna a função wrapper

@time_performance       # Indica ao python que a função do_this() terá um comportamento diferente
def do_this():
    # Simulando running code
    time.sleep(1.3)

@time_performance       # wrapper será chamado quando do_that() for chamado
def do_that():
    # Simulando running code
    time.sleep(0.4)

do_this()
do_that()
print('Done')


#pylint:disable-all