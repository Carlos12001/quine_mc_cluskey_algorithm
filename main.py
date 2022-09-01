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


if __name__ == "__main__":
    num_var = 4
    lista = [12, 1, 15, 7, 6]
    print(lista)
    lista = lista_entero_a_bin(lista)
    print(lista)
    lista = ordena_lista_por_1s(lista)
    print(lista)
    print(lista_bin_a_entera(lista))
