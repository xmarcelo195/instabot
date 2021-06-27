# enviar as postagens agendadas para o creator studio

#importar bibliotecas
import pandas as pd
from selenium.webdriver.common.keys import Keys
from creator_studio.creator_studio import CreatorStudio

#fazer login
cs_cli = CreatorStudio("login", "senha")
cs_cli.login()

#localização da planilha da organização dos posts
file_location = r"D:\Linux\pycharm\data\instabot\insta_sobremesas\calendario\postagens.csv"
df = pd.read_csv(file_location, sep=';')
# /\ colunas do csv ['img', 'txt', 'data', 'conta', 'horarios']

hashtags= "\n#receita #sobremesa #sobremesas #adorocozinhar #cozinharcomamor #doces #doce #receitas #amochocolate #receitasfaceis #receitafacil"

# agendar postagens
for index, row in df.iterrows():
    with open(row['txt'], "r", encoding="utf8") as f:
        text = f.read()
    text = text + hashtags
    cs_cli.create_post(account=row['conta'],
                       message=text,
                       file=row['img'],
                       schedule_options={
                           "date": row['data'],
                           "time": row['horarios']
                       },
                       social_network='instagram')


