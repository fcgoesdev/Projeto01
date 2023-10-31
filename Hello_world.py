def somar_numeros(numero1, numero2):
    numero1 = input('Digite um número:')
    numero2 = input('Digite outro número:')
    print(numero1 + numero2)


print('Hello World!!!')

frase = "Eu amo programar em Python !!!"

for i in frase:
    print(i)

bombons = 10

while bombons > 0:
    if bombons > 1:
        print(f"Eu tenho {bombons} Bombons.")
    else:
        print(f"Eu tenho {bombons} Bombom.")
    bombons = bombons - 1
    print(f"Comi 1 Bombom e fiquei com {bombons}!!!")

somar_numeros(15, 20)

