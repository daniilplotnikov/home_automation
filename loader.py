import os
import time
select_do=input(print("Что бы вы хотели сделать?"))
print ("Доступные пункты: установка модулей.")
if select_do=="Установка модулей.":
 os.system ("python run_modules.py")
else:
 print ("Данного пункта не сущестует!")