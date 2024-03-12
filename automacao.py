import pyautogui

contador: int
contador = 0

while contador <= 20:

    pyautogui.PAUSE = 0.5

    pyautogui.press('enter')

    contador += 1