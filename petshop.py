# Função para definir o valor base
def cachorro_peso():
    while True:
        # Validação dos dados
        try:
            peso = int(input("Insira o peso do cachorro: "))
        except ValueError:
            print("Você não digitou um valor numérico.\n")
            continue
        if peso >= 50:
            print("Não aceitamos cachorros com esse porte\n")
            continue
        elif peso < 0:
            print("Esse peso é inválido\n")
            continue
        print("")

        # Se chegou nesse ponto o dado inserido é válido
        if peso < 3:
            base = 40
            return base
        elif 3 <= peso < 10:
            base = 50
            return base
        elif 10 <= peso < 30:
            base = 60
            return base
        else:
            base = 70
            return base

# Função para definir o multiplicador
def cachorro_pelo():
    while True:
        tampelo = input("Qual é o tamanho do pelo do seu cachorro:\ncurto(c)\nmédio(m)\nlongo(l)\n=>")
        print("") # Print vazio para a formatação

        # Validação do valor inserido
        if tampelo.lower() not in "cml" or tampelo == "":
            print("Tamanho de pelo inválido, tente novamente")
            continue

        # Transformação do input para minúscula e verificação do valor inserido
        tampelo = tampelo.lower()
        if tampelo == "c":
            multiplicador = 1
            return multiplicador
        elif tampelo == "m":
            multiplicador = 1.5
            return multiplicador
        else:
            multiplicador = 2
            return multiplicador

# Função para definir os adicionais
def cachorro_extra():
    extra = 0
    while True:
        adicional = input("Deseja adicionar algum serviço?\nCortar as unhas(1) R$ 10,00"
                          "\nEscovar os dentes(2) R$ 12,00"
                          "\nLimpar as orelhas(3) R$ 15,00"
                          "\nSair(0)"
                          "\n=>")

        # Validação do valor inserido
        if adicional not in "1230": # Não há necessidade de converter para int, então usei como str
            print("Adicional inválido")
            print("")
            continue

        # Verificação do valor inserido
        if adicional == "1":
            extra += 10
        elif adicional == "2":
            extra += 12
        elif adicional == "3":
            extra += 15
        else: # Nesse caso o adicional é "0"
            break
        print("")
    return extra

# Programa principal
print("Bem vindo ao petshop do Marco Antonio Ferreira Pinto")
vlrbase = cachorro_peso()
vlrmult = cachorro_pelo()
vlrextra = cachorro_extra()

total = (vlrbase * vlrmult) + vlrextra
print(f"O total a pagar é de R$ {float(total)} . (peso: {vlrbase} * pelo: {vlrmult} + adicionais: {vlrextra})")