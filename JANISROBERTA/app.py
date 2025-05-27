'''Python'''
# Arrays (vetores/matrizes utilizando a blibioteca NumPY)
import numpy as np

# Criando um array NumPY unidimensional a partir  de uma lista 
array = np.array([1, 2, 3, 4, 5])
print ("Array:"array)

# Acessando elemnetos do arraya:
# - Indices ccomeçam com 0 
# - indices negativos acessam a partir do final 
print("Primeiro elemento:", array [0])
print("Último elemento:", array[-1])
# Slincing (fatiamento) de arrys:
# - Sintaxe: [início:fim]
# - O índice final não é incluído
print("Elementos do índice 1 a 3 (exclusivo):", array[1:3])
# Listas (estrutura mutável de elementos)
# Criando uma lista básica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)


# Adicionando um elemento ao final da lista
my_list.append(6)
print("Lista após adicionar 6:", my_list)

# Inserindo um elemento em posição específica:
# - Sintaxe: insert(índice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("Lista após inserir 7 na posição 2:", my_list)

# Removendo a primeira ocorrência de um elemento
my_list.remove(4)
print("Lista após remover o valor 4:", my_list)
# Tuplas (estrutura imutável de elementos)
# Criando uma tupla - usa parênteses ao invés de colchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tupla:", my_tuple)

# Acesso a elementos funciona igual às listas
print("Primeiro elemento da tupla:", my_tuple[0])
print("Último elemento da tupla:", my_tuple[-1])

# Loops (estruturas de repetição)

# Loop for iterando sobre elementos de uma lista
fruits = ["maçã", "banana", "morango"]
print("Frutas na lista:")
for fruit in fruits:
    print(fruit)

# Loop while executando enquanto condição é verdadeira
print("Contagem de 0 a 4:")
i = 0
while i < 5:
    print(i)
    i += 1  # Incrementa o contador

# Loop for com acesso ao índice e elemento simultaneamente usando enumerate
print("Elementos da lista com seus índices:")
my_list = [1, 2, 3, 4, 5]
for indice, elemento in enumerate(my_list):
    print(f"Índice {indice}: {elemento}")

