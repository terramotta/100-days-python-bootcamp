# Generate a list

## Using a for loop
def create_list_using_for_loop(n):
    my_list = []
    for x in range(n):
        my_list.append(x)
    return my_list

## Using list comprehension     -> Plus efficient, plus readable
def create_list_using_list_comprehension(n):
    return [x for x in range(n)]

import dis
dis.dis(create_list_using_for_loop)
dis.dis(create_list_using_list_comprehension)

# Com os bytecodes conseguimos ver que a list comprehension é mais eficiente, pois
# tem menos instruções para serem executadas para adicionar os elementos na lista














#pylint: disable-all