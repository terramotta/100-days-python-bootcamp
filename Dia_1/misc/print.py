# print(object(s), sep=separator, end=end, file=file, flush=flush)

#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#     obkect(s) - any object, and as many as you like. Will be converted to string before printed
#     sep - separator, default is ' '
#     end - end, default is '\n'
#     file - a file-like object (stream); defaults to the current sys.stdout (a tela)
#     flush - whether to forcibly flush the stream. Default is False.

'''
Quando flush é definido como True, ele instrui o programa a limpar o buffer imediatamente após cada chamada da função print().
Isso significa que os dados no buffer são enviados para a tela imediatamente, em vez de aguardar até que o buffer esteja cheio
ou até que a execução do programa termine.  Isso pode ser útil em situações em que você deseja ver a saída em tempo real, como
quando você está monitorando o progresso de um processo.

Por outro lado, quando flush é False (o padrão), o buffer não é limpo automaticamente após cada chamada da função print().
Isso significa que os dados podem permanecer no buffer por um tempo, aguardando até que o buffer esteja cheio ou até que o
programa termine antes de serem enviados para a saída.
'''

# Exemplo 1: Exibindo variáveis
nome = "Alice"
idade = 30
print("Nome:", nome)
print("Idade:", idade)

# Exemplo 2: Concatenando strings
nome = "Bob"
idade = 25
print("Nome: " + nome + ", Idade: " + str(idade))

# Usando placeholders
nome = "Carol"
idade = 20
print("Nome: %s, Idade: %d" % (nome, idade))

# pylint: disable=all