import pyautogui 
mensagem = str(input('Digite a mensagem'))
pyautogui.press('winleft')
pyautogui.sleep(2)
pyautogui.write('word')
pyautogui.sleep(5)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.write(mensagem)
