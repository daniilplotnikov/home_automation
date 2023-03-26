import os
import yaml
from pprint import pprint

with open('zigbee2mqtt.yaml') as f:
    templates = yaml.safe_load(f)
pprint(templates)
if templates==[{'zigbee2mqtt': {False: None}}]:
 directory=os.getcwd()
 zigbee=(directory + '/modules/zigbee2mqtt')
 os.chdir(zigbee)
 os.system("bash start.sh")