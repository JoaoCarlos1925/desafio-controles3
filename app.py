import time
import os

def clear_screen():
    # Limpa a tela no Windows
    if os.name == 'nt':
        os.system('cls')
    # Limpa a tela no Linux/macOS
    else:
        os.system('clear')

while True:
    # Solicita que o usuário digite um número
    numero = input("Digite um número para iniciar a contagem regressiva (ou 0 para sair): ")
    
    # Verifica se a entrada é um número válido
    if not numero.isdigit():
        print("Por favor, digite um número válido.")
        continue

    numero = int(numero)
    
    # Verifica se o usuário quer sair
    if numero == 0:
        print("Saindo do programa.")
        break

    # Realiza a contagem regressiva
    for i in range(numero, -1, -1):
        clear_screen()
        print(i)
        time.sleep(1)
    print()
