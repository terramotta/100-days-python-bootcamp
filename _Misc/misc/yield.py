## Maneira tradicional:
def fetch_lines(filename):
    with open(filename ,'read') as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines

## Maneira mais eficiente:
def fetch_lines_2(filename):
    with open(filename ,'read') as file:
        for line in file:
            yield line

zen = fetch_lines_2('zen.txt')
# Dessa forma, o código é mais eficiente, pois não carrega todas as linhas do arquivo
# na memória, mas sim, apenas uma por vez.

# Por conta do keyword yield, a função se tornou um generator, e zen se tornou um objeto
# generator.
# A linha está yielding em yield line até que chamemos next(zen) para obter a próxima linha.abs

# Quando chamo next(zen), a função fetch_lines_2 continua a partir do ponto onde parou.



#pylint: disable-all