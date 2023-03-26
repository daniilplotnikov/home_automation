import yaml
with open('web.yaml') as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
if read_data==[{'web': {True: None}}]:
    print ("данная функция в разработке!")