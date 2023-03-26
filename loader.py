import os
print ("Доступные пункты: установка модулей.")
os.system ("python run_system_module.py")
select_do=input(print("Что бы вы хотели сделать?"))
if select_do=="Установка модулей.":
 os.system ("python run_modules.py")
else:
 print ("Данного пункта не сущестует!")