import pyautogui as pg
import webbrowser as web
from time import sleep
import os

os.system("clear")

print('''
BANNER EN REPARACION!!!
__                     _        __           _
/ _| _ _   _ _ _ _ _\ \      / / |_   _ | | _
\__ \| ' \ / ` | ' ` _ \ \ /\ / /| '_ \ / ` | _/ __|
 _) | |) | (| | | | | | \ V  V / | | | | (| | |\__ \
 
|_/| ./ \,|| || ||\/\_/  || ||\_,|\_|__/
      |_|
''')
    
numero = int(input("Inserte un numero +"))
print("")
texto = str(input("Texto a enviar: "))
web.open("https://web.whatsapp.com/send?phone=+{}".format(numero))
sleep(10)
while True:
    sleep(1)
    pg.typewrite(texto)
    pg.press("enter")

#Fin
