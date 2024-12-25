import pyautogui

# Localizar o campo de nome e preencher
pyautogui.moveTo(10, 10, duration=0.25)  # Mover o mouse para a posição do campo de nome
pyautogui.click()  # Clicar no campo
pyautogui.write("Seu Nome Aqui")  # Digitar o nome

# Localizar o botão de envio e clicar
pyautogui.moveTo(10, 10, duration=0.25)  # Mover o mouse para o botão
pyautogui.click()  # Clicar no botão

print("Formulário enviado!")