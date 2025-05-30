'''1 – Para treinar o laço de repetição FOR, crie um formulário e peça para o usuário digitar
um número inicial e um número final, mostre o intervalo entre esses números, mas
lembre-se que ele poderá digitar um intervalo muito grande que irá consumir muita
memória do servidor, pensando nisso valide para que ele digite apenas intervalos de no
máximo 100 números.'''


numeroInicial = int(input("Digite o numero inicial: "))
numeroFinal = int(input("Digite o numero final: "))

tamanhoIntervalo = numeroFinal - numeroInicial

if tamanhoIntervalo > 100:
    print("Não pode ser maior do que 100")
else:
    for i in range(numeroInicial + 1, numeroFinal):
        print(str(i)) 
