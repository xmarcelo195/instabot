import pandas as pd
import os
import numpy as np
import datetime
from itertools import cycle

# config inciciais
posts_dia = 3
conta = 'sobremesas_diarias'

diretorio = r'D:\Linux\pycharm\data\instabot\insta_sobremesas\calendario\receitas_da_semana'
arquivos = os.listdir(diretorio)

lista_nomes = []
for item in arquivos:
    lista_nomes.append(item[:-4])

lista_unique = list(set(lista_nomes))

df = pd.DataFrame(lista_unique, columns=['nomes'])

# criação das datas
data_inicial = datetime.datetime.now() + datetime.timedelta(days=1)
nova_data = data_inicial
datas = []
i = 1
for x in range(len(lista_unique)):
    datas.append("{}/{}/{}".format(nova_data.month, nova_data.day, nova_data.year))

    if i >= posts_dia:
        i = 1
        nova_data += datetime.timedelta(days=1)
        continue
    i += 1

# criação horários 5:00 P
horarios = cycle(['1:00 P', '3:00 P', '6:00 P'])

# criação dataframe
df['img'] = diretorio + '\\' + df['nomes'].astype(str) + '.jpg'
df['txt'] = diretorio + '\\' + df['nomes'].astype(str) + '.txt'
df['data'] = pd.DataFrame(datas)
df['conta'] = conta
df['horarios'] = [next(horarios) for count in range(df.shape[0])]
del df['nomes']

df.to_csv('D:\\Linux\\pycharm\\data\\instabot\\insta_sobremesas\\calendario\\postagens.csv', sep=';',
          encoding='utf-8-sig', index=False)

