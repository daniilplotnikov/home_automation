import os
import eel

@eel.expose
def add_module(select_module:str):
    return (select_module)
available_module="zigbee"
print (available_module)
select_module=(input(print("Введите нужный модуль:")))
if select_module=="zigbee":
    zigbee=('modules/zigbee')
    os.chdir(zigbee)
    os.system("python application.py")
