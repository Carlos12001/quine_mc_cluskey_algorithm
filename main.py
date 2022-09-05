num_var = 0


def entero_a_bin(num_entero):
    global num_var
    return format(num_entero, "0" + str(num_var) + "b")


def lista_entero_a_bin(lista_entera):
    lista_binaria = []
    for i in lista_entera:
        lista_binaria += [entero_a_bin(i)]
    return lista_binaria


def lista_bin_a_entera(lista_binaria):
    lista_entera = []
    for i in lista_binaria:
        lista_entera += [int(i, 2)]
    return lista_entera


def ordena_lista_por_1s(lista_minterminos):
    lista_minterminos.sort(key=lambda num: (num.count("1"), num))
    return lista_minterminos


def se_diferencia_un_digito(num_bin_1, num_bin_2):
    contador = 0
    for i in range(len(num_bin_1)):
        if num_bin_1[i] != num_bin_2[i]:
            contador += 1
    return contador == 1


# Funcion que se encarga de remplzar el bit complementario
def remplaza_complementos(num_bin_1, num_bin_2):
    resultado = ""

    for i in range(len(num_bin_1)):
        if num_bin_1[i] != num_bin_2[i]:
            resultado = resultado + "-"
        else:
            resultado = resultado + num_bin_1[i]

    return resultado


def prueba():
    global num_var
    num_var = 4
    lista = [12, 1, 15, 7, 6]

    # Paso 1
    print("Prueba paso 1")
    print(lista)
    lista = lista_entero_a_bin(lista)
    print(lista, "\n\n")

    # Paso 2
    print("Prueba paso 2")
    lista = ordena_lista_por_1s(lista)
    print(lista)
    print(lista_bin_a_entera(lista), "\n\n")

    # Paso 3
    print("Prueba paso 3")
    print("Se diferencia por un solo digito", "1000", "1010")
    print(se_diferencia_un_digito("1000", "1010"))
    print("Se diferencia por un solo digito", "0000", "1010")
    print(se_diferencia_un_digito("0000", "1010"), "\n\n")

    # Paso 4
    print("Prueba paso 4")
    print("Remplaza los bits complementarios de", "1000", "1010")
    print(remplaza_complementos("1000", "1010"))
    print("Remplaza los bits complementarios de", "1010", "1010")
    print(remplaza_complementos("1010", "1010"), "\n\n")


if __name__ == "__main__":
    prueba()
