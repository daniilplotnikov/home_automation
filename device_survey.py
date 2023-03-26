import yaml
from pprint import pprint

with open('database.yaml') as f:
    templates = yaml.safe_load(f)

if templates=="None":
    print ("Недопустимая конфигурация yaml!")
else:
    print ("Текущая база данных содержит следующие данные:",templates)