#este proyecto consta de enviar mensajes de whatsapp usando python

#primer paso tener instaldo previamente pyautogui y posteriormente importarlo 
import pyautogui, webbrowser  #webbrowser sirve para poder ingresar a una pagina web 
from time import sleep # sleep sirve para poder dar un tiempo de espera
#la siguiente linea da la instrucción de abrir la pagina web y mandar un mensaje al numero que se indique
#el numero se debe de agregar con la lada del lugar donde se encuentre
webbrowser.open("https://web.whatsapp.com/send?phone=+52************") 

sleep(10)# hará que espere 10 segundos para empezar a mandar los mensajes
#se hace un ciclo for donde agregamos un rango de mensajes 
for i in range(30): #se enviaran 30 mensajes 
	pyautogui.typewrite("prueba")#la función typewrite escribira el mensaje que le indiquemos de manera automatico
	pyautogui.press("enter")# con la función prees indicamos que pulse la tecla enter al terminar de escribir el mensaje