from unidade_federativa import Unidade_Federativa

unestados = Unidade_Federativa.get_lista_uf()
unuf = Unidade_Federativa.get_uf()

print("LISTA DE ESTADOS")
for counter, value in enumerate(unestados):
    print(counter,"-", value)

for counter, value in enumerate(unuf):
    sigla = input("Escolha o Estado para descobrir a UF: ")
    if (sigla == "0"):
        print("A UF do Estado de " + unestados[0] + " é " + unuf[0])
    elif (sigla == "1"):
        print("A UF do Estado do " + unestados[1] + " é " + unuf[1])
    elif (sigla == "2"):
        print("A UF do Estado do " + unestados[2] + " é " + unuf[2])
    elif (sigla == "3"):
        print("A UF do Estado d0 " + unestados[3] + " é " + unuf[3])



