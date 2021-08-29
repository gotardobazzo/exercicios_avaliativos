from unidade_federativa import Unidade_Federativa

unestados = Unidade_Federativa.get_lista_uf()
unuf = Unidade_Federativa.get_uf()

for counter, value in enumerate(unestados):
    print(counter, value)

for counter, value in enumerate(unuf):
    sigla = input("Escolha a numeracao do estado que deseja saber a UF: ")
    if (sigla == "0"):
        print("A UF do estado selecionado é: " + unuf[0])
    elif (sigla == "1"):
        print("A UF do estado selecionado é: " + unuf[1])
    elif (sigla == "2"):
        print("A UF do estado selecionado é: " + unuf[2])
    elif (sigla == "3"):
        print("A UF do estado selecionado é: " + unuf[3])


