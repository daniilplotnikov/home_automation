import os
available_module="zigbee2mqtt"
print (available_module)
directory=os.getcwd()
select_module=(input(print("Введите нужный модуль:")))
if select_module=="zigbee2mqtt":
    zigbee=(directory + '/modules/zigbee2mqtt')
    os.chdir(zigbee)
    os.system("bash install.sh")
else:
  print("Такого модуля не существует, либо он не введён в этот файл.") 