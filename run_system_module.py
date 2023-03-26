import os
directory=os.getcwd()
zigbee=(directory + '/modules/zigbee2mqtt')
os.chdir(zigbee)
os.system("bash start.sh")
