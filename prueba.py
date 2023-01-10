import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+525585616349")

sleep(10)

for i in range(25):
	pyautogui.typewrite("prueba")
	pyautogui.press("enter")