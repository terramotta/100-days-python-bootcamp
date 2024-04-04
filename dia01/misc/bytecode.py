# pylint: disable=all
import dis

def operacao_complexa(x, y, z):
    resultado = (x + y) * z
    return resultado

dis.dis(operacao_complexa)

# Obtém o bytecode da função como uma lista de strings
bytecode_str = dis.Bytecode(operacao_complexa).dis()

# Salva o bytecode em um arquivo de texto
with open("bytecode.txt", "w") as arquivo:
    arquivo.write(bytecode_str)


#  1           0 RESUME                   0
#
#  2           2 LOAD_FAST                0 (x)
#              4 LOAD_FAST                1 (y)
#              6 BINARY_OP                0 (+)
#             10 LOAD_FAST                2 (z)
#             12 BINARY_OP                5 (*)
#             16 STORE_FAST               3 (resultado)
#
#  3          18 LOAD_FAST                3 (resultado)
#             20 RETURN_VALUE
