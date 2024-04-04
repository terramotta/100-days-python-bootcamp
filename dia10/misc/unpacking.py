def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
print(*coins) # Output: 100 50 25

# No caso de argumentos para funções, o próprio python cuida de colocar as vírgulas entre os argumentos.
print(total(*coins)) # Unpacking the list
# Maneira menos legível: >>> print(total(coins[0], coins[1], coins[2]))


coins_dic = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins_dic)) # Unpacking the dictionary
# Essa sintaxe tem o efeito de passar 3 valores com nomes: galleons=100, sickles=50 e knuts=25.abs
# Ou seja, passa as keys e os valores "separados" por um sinal de igual.
# Maneira menos legível: >>> print(total(coins_dic["galleons"], coins_dic["sickles"], coins_dic["knuts"])) # Output: 17425



#pylint: disable-all