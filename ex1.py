numeroInicial = int(input("Digite o número inicial: "))
numeroFinal = int(input("Digite o numero final: "))

tamanhoIntervalo = numeroFinal - numeroInicial

if tamanhoIntervalo > 100:
    print("Não pode ser maior do que 100")
else:
    for i in range(numeroInicial + 1, numeroFinal):
        print(str(i))
