'''2 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 100.'''

for i in range(1, 100):
    if i % 2 != 0:
      print(str(i))

    


''' i é frequentemente usada como contador para controlar o número de iterações. Ela é um índice que indica a posição atual dentro de uma sequência, como uma lista, string ou intervalo de números. '''

i = 1
while i <=100: 

   if i % 2 != 0:
      print(str(i))
   i+= 1
