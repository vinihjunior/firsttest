from random import randint

while True:
    print("\nDescubra qual é o animal: ")
    lista = ["cachorro", "gato", "cavalo", "elefante", "arara", "galinha"]
    end = len(lista)
    secret = randint(0, end - 1)
    animal = (lista[secret])

    print("\nQue tem", len(animal), "letras \n",
          "\nE começa com a letra", animal[0], "\n")
    resp = input("\nDigite sua resposta: ")
    if resp == animal:
        print("Você ACERTOU!!, é", animal, "\n")
        break
    else:
        print("\nVocê errou :(\n")
        voltar = input("Deseja voltar? (y/n): ")
        if voltar not in ("y" or "Y"):
            break
