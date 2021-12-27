import pyautogui as pg
import webbrowser as web
from time import sleep
import os
try:
    os.system("cls")
except:
    os.system("clear")

numero = int(input("Inserte un numero sin el simbolo + : "))
print("")
texto = str(input("Texto a enviar: "))
web.open("https://web.whatsapp.com/send?phone=+{}".format(numero))
sleep(10)
while True:
    sleep(1)
    pg.typewrite(texto)
    pg.press("enter")

#Fin