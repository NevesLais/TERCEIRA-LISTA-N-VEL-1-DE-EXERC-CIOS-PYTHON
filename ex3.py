'''3 – Peça para o usuário digitar um número, e mostre para ele se aquele é um número
primo ou não.''' '''para ser primo so divide por 1 e por ele msm'''

numero = int(input("Digite um número: "))

primo = True

i = numero

while i > 1:
    if numero % i == 0 and numero != i and numero != 1:
        primo = False
    i = i - 1
    
if primo:
    print("É um número primo")
else:
    print("Não é um número primo") 
