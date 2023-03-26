import os
import time
print ("Доступные пункты: установка модулей.")
os.system ("python device_survey.py")
select_do=input(print("Что бы вы хотели сделать?"))
if select_do=="Установка модулей.":
 os.system ("python run_modules.py")
else:
 print ("Данного пункта не сущестует!")