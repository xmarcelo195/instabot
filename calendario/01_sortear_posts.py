import os
import numpy as np

source = r'D:\Linux\pycharm\data\instabot\insta_sobremesas\calendario\todas_receitas'
dest = r'D:\Linux\pycharm\data\instabot\insta_sobremesas\calendario\receitas_da_semana'

lista = os.listdir(source)
lista_nomes = []
for item in lista:
    lista_nomes.append(item[:-4])

lista_unique = list(set(lista_nomes))
n_publi = int(input('Quantas publicacoes pegar? (default=21): '))

i = 0
while i < n_publi:
    index = np.random.randint(0, (len(lista_unique)))
    n_sort = lista_unique.pop(index)
    os.rename(source + '\\' + n_sort + '.jpg', dest + '\\' + n_sort + '.jpg')
    os.rename(source + '\\' + n_sort + '.txt', dest + '\\' + n_sort + '.txt')
    i += 1
