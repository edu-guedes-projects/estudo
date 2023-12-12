# IMPORTANTE!!!

# Comando para saber a versão do Python que está instalada:
# - No terminal, digite python --version

# Se digitar só python, entrará no ambiente de interpretação do python, que serve para rodar os scripts python. Para sair, digite Ctrl + Z e pressione Enter.

# A identação é de suma importância no python, pois se o código não estiver corretamente identado, ele não funcionará.

# Os comentários, em python, são sempre precedidos de hashtag (#).


# VARIÁVEIS:

# - Todas as variáveis são objetos;
# - Não precisam ser declaradas;
# - São criadas no momento em que lhe atribuímos um valor;
# - Seu nome tem que começar por uma letra;
# - Seu nome não pode começar por um número;
# - Seu nome só pode conter caracteres, algarismos e underscores;
# - Seu nome é case-sensitive;


# NÚMEROS:

# valor1 = 10 (int – positivos e negativos sem limite)
# valor2 = 2.5 (float – positivos ou negativos com valores decimais)
# Valor3 = 1j (complexos – usados em cálculos matemáticos)

# E para imprimir: print(nome_da_variável)


# STRINGS:

# nome = 'Eduardo'
# sobrenome = 'Guedes'

# E para imprimir: print(nome + ' ' + sobrenome)

# Concatenação inválida:

# valor1 = 10
# valor2 = "20"
# print(valor1 + valor2)

# Atribuição:

# a, b, c = 10, 20, 30
# print(a + b + c)

# z = x = y = "João"
# print(x)

# Conversão:

# valor1 = 10
# valor2 = “20”
# valor3 = int(valor2)
# print(valor3)

# Também podemos fazer isto:

# valor1 = 10
# valor2 = “20”
# print(valor1 + int(valor2))

# Obs. - Referente à strings, podemos ter a seguinte situação:

# frase = '''primeira linha
# segunda linha
# terceira linha'''
# print(frase)


# OPERADORES MATEMÁTICOS:

# a = 20
# b = 10

# resultado = a + b  -> Adição
# resultado = a - b  -> Subtração
# resultado = a * b  -> Multiplicação
# resultado = a / b  -> Divisão
# resultado = a % b  -> Resto da divisão
# resultado = a ** b -> Exponenciação
# resultado = a // b -> Arredondamento do resto
# print(resultado)


# OPERADORES DE ATRIBUIÇÃO:

# valor = 2  -> valor é igual a 2
# valor += 2 -> valor é igual ao seu valor mais 2
# valor -= 2 -> valor é igual ao seu valor menos 2
# valor *= 2 -> valor é igual ao seu valor multiplicado por 2
# valor /= 2 -> valor é igual ao seu valor dividido por 2
# valor %= 2 -> valor é igual ao resto da divisão do seu valor por 2
# print(valor)


# OPERADORES DE COMPARAÇÃO:

# valor1 = 10
# valor2 = 20

# resultado = valor1 == valor2 -> Falso
# resultado = valor1 != valor2 -> Verdadeiro
# resultado = valor1 > valor2  -> Falso
# resultado = valor1 < valor2  -> Verdadeiro
# resultado = valor1 >= valor2 -> Falso
# resultado = valor1 <= valor2 -> Verdadeiro
# print(resultado)


# LISTAS (COLEÇÕES DE DADOS)

# List - coleção ordenada, alterável e que permite valores duplicados.

# lista = ['Eduardo', 'Maria', 'Leonardo']

# Para apresentar valores de uma lista:
# print(lista)
# print(lista[0])

# Para alterar valores de uma lista:
# lista[2] = 'Ana'
# print(lista[2])

# Iteração por todos os valores:
# for nome in lista:
# 	print(nome)

# Para verificar se um item existe na lista:
# if 'Eduardo' in lista:
#	  print('Existe!')
# else:
# 	print('Não existe!')

# Para verificar a quantidade de elementos em uma lista:
# print(len(lista))

# Para adicionar itens à lista:
# lista.append('Vitor')
# print(lista)

# Para remover itens de uma lista:
# lista.remove("Eduardo")
# print(lista)

# Para remover um índice específico ou o último elemento:
# lista.pop()
# print(lista)

# Para remover com del:
# del lista[1]
# print(lista)

# Para remover toda a lista:
# del lista
# print(lista) -> Esse comando print não funcionará, pois a lista não existe mais a partir do comando del lista!

# Para limpar a lista:
# lista.clear()
# print(lista)

# Para copiar uma lista:
# lista2 = lista.copy()
# print(lista2)

# Tuple – coleção ordenada mas inalterável que permite valores duplicados.

# lista = ('Eduardo', 'Maria', 'Leonardo')
# print(lista)

# Acessar os valores do tuple:
# print(lista[1])

# Não é possível alterar valores!!!
# lista[1] = 'Rosana'

# *** NÃO PODEMOS EDITAR, ADICIONAR OU REMOVER ITENS DO TUPLE!!! ***

# Set – coleção desordenada e sem índice que não permite valores duplicados.

# *** NÃO PODEMOS ACESSAR OS ELEMENTOS DO SET PELO SEU ÍNDICE!!! ***

# Para verificar se um item existe no set:
# if 'Eduardo' in lista:
# 	print('OK!')

# Resumindo o código acima:
# print('Eduardo' in lista)

# Para atualizar o set:
# lista = {'Edu', 'Léo'}
# print(lista)

# Para adicionar elementos ao set:
# lista.add('Cristina')
# print(lista)

# Para adicionar vários elementos ao set:
# lista.update(['Rui', 'José'])
# print(lista)

# Para remover um elemento do set:
# lista.remove('Elemento')

# *** O MÉTODO ACIMA PODERÁ DAR UM ERRO CASO O ELEMENTO NÃO EXISTA NO SET!!! ***

# Para remover com discard:
# lista.discard('Elemento')

*** O método acima não dá erro, pois se o elemento não existir no set, nada acontece!!!

Para remover com pop:
nome = lista.pop()
print(nome)
print(lista)

Para limpar o set:
lista.clear()
print(lista)

Para remover o set:
del lista
print(lista)

Dictionary – Coleção desordenada, alterável e indexada. Não permite valores duplicados.
lista = {
	“nome”:”Eduardo”,
	“sobrenome”:”Guedes”,
	“altura”: 182
	}
print(lista)

Para acessar os itens do dictionary separadamente:
print(lista[‘sobrenome’])
ou
print(lista.get(‘nome’))

Para alterar valores do dictionary:
lista[‘sobrenome’] = “Brasbie”
print(lista.get(‘sobrenome’))

Para iterar por todos os elementos mostrando as keys:
for item in lista:
	print(item)


Para iterar por todos os elementos mostrando os valores:
for item in lista:
	print(lista.get(item)) ou
	print(lista[item])

Outra forma:
for item in lista.values():
	print(item)

Iteração por keys e values:
for key, valor in lista.itens():
	print(key, valor)

Para verificar se uma chave existe dentro do dictionary:
if ‘nome’ in lista:
	print(lista.get(‘nome’))

Para adicionar elementos ao dictionary:
lista[‘nacionalidade’] = “brasileira”
print(lista)

Para remover itens do dictionary:
lista.pop(‘nome’)
print(lista)

Para remover o último item do dictionary:
lista.popitem()
print(lista)

Para remover com del:
del lista[‘sobrenome’]
print(lista)

Para eliminar tudo (remover o dictionary):
del lista
print(lista)

Para limpar o dictionary:
lista.clear()
print(lista)
