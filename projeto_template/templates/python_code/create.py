# colocar template em todas as fotos baixadas

#importar bibliotecas que serão usadas
from PIL import Image
import os
from tqdm import tqdm

path = 'D:\\Linux\\pycharm\\data\\instabot\\insta_sobremesas\\projeto_template\\templates\\exemplo\\'
listdir = os.listdir(path)
background = Image.open('../fundo.png')

#templates que serão utilizados
template1 = Image.open(r'D:\Linux\pycharm\data\instabot\insta_sobremesas\projeto_template\templates\Final\temp1.png')
template2 = Image.open(r'D:\Linux\pycharm\data\instabot\insta_sobremesas\projeto_template\templates\Final\temp2.png')
template3 = Image.open(r'D:\Linux\pycharm\data\instabot\insta_sobremesas\projeto_template\templates\Final\temp3.png')

templates = [template1, template2, template3]

i = 0

#pegar as fotos na pasta e colocar nos templates
for file in tqdm(listdir):
    if file[-4:] == '.jpg':
        foto = Image.open(path + file)
        image = background.copy()
        foto_resized = foto.resize((900, 900), Image.ANTIALIAS)
        image.paste(foto_resized, (50, 50))
        image.paste(templates[i], (0, 0), templates[i])
        rgb_im = image.convert('RGB')
        rgb_im.save(path + file[:-4] + '.jpg')
        if i >= 2:
            i = 0
        else:
            i += 1
