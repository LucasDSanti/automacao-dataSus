import pyautogui

contadorFormulario: int
contadorFormulario = 1

contadorEnter: int

contadorMedicamento: int

pyautogui.alert('IREI COMEÇAR A DAR ENTER EM 3 SEGUNDOS!')
pyautogui.PAUSE = 3

while contadorFormulario <= 5:

    contadorEnter = 1
    contadorMedicamento = 1

    while contadorEnter <= 34:

        pyautogui.press('enter')
        pyautogui.PAUSE = 0.5

        contadorEnter += 1

    pyautogui.press('esc')

    contadorEnter = 1

    while contadorEnter <= 24:

        pyautogui.press('enter')

        if contadorEnter == 3:

            try: pyautogui.locateOnScreen('estadioUicc.png')
        
            except: print("NÃO ACHEI!")

            else: 
                print("ACHEI!") 
                contadorEnter += 1

        if contadorEnter == 13 and contadorMedicamento == 1:

            try: pyautogui.locateAllOnScreen('medicamento4.png')

            except: 
                print("NÃO ACHEI!")
                contadorEnter = contadorEnter - 4
                contadorMedicamento += 1

            else: 
                print("ACHEI!")

        contadorEnter += 1

    pyautogui.press('down')

    contadorFormulario += 1