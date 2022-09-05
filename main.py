import timeit

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


# Funcion revisa si ya este numero binario exite dentro los minterminos
def dentro_de_la_lista(lista_minterinos, num_bin):
    for i in lista_minterinos:
        if i == num_bin:
            return True
    return False


# Simplifica la lista de minterminos
def reduce(lista_minterminos):
    nuevos_minterminos = []  # Lista de minterminos reducida
    n = len(lista_minterminos)  # Largo de la lista
    """
    Lista incia 0's de n elementos ya que ningún mintermino ha cambiado
    ha hecho paraja con otro mintérmino. Cuando lo encuentre pasa a ser 1.
    """
    cual_mintermino_cambio = [0] * n

    # Paso 5
    for i in range(n):
        for j in range(n):
            if se_diferencia_un_digito(lista_minterminos[i],
                                       lista_minterminos[j]):
                cual_mintermino_cambio[i] = 1
                cual_mintermino_cambio[j] = 1
                nuevo_num_bin = remplaza_complementos(lista_minterminos[i],
                                                      lista_minterminos[j])
                # Paso 6
                if not dentro_de_la_lista(nuevos_minterminos, nuevo_num_bin):
                    nuevos_minterminos.append(nuevo_num_bin)

    # Se agrega todos los terminos reducidos a la lista
    for i in range(n):
        # Paso 6
        if (cual_mintermino_cambio[i] != 1 and (
                not dentro_de_la_lista(nuevos_minterminos,
                                       lista_minterminos[i]))):
            nuevos_minterminos.append(lista_minterminos[i])

    # Finaliza el Paso 5
    return nuevos_minterminos


# Algoritmo de Quine McCluskey
def quine_mc_cluskey(num_literales, minterminos):
    global num_var

    num_var = num_literales
    lista_minterminos = []

    lista_minterminos = lista_entero_a_bin(minterminos)
    lista_minterminos = ordena_lista_por_1s(lista_minterminos)

    # Se repite el Paso 5 hasta que se encuentre todos los primos esenciales
    while True:
        lista_minterminos = reduce(lista_minterminos)
        ordena_lista_por_1s(lista_minterminos)
        if lista_minterminos == reduce(lista_minterminos):
            break

    # Paso 7
    return lista_minterminos


# Muestra el implicante en su representacion booleana
def obtenga_literal(minterminos):
    global num_var
    resultado = ""
    variables = ["a", "b", "c", "d", "e", "f", "g", "h"]
    no_importa = "-" * num_var

    if minterminos == no_importa:
        return "1"
    else:
        for i in range(len(minterminos)):
            if minterminos[i] != "-":
                if minterminos[i] == "0":
                    resultado = resultado + variables[i] + "\'"
                else:
                    resultado = resultado + variables[i]

        return resultado


# Realiza la representacion booelana funcional de la suma de minterminos
def obtenga_funcion(lista_minterminos):
    resultado = ""
    for i in lista_minterminos[:len(lista_minterminos) - 1]:
        resultado += obtenga_literal(i) + " + "
    resultado += obtenga_literal(lista_minterminos[-1])
    return resultado


# Función que calcula tiempo de otras funciones
def calcula_tiempo(funcion, *args):
    inicio = timeit.default_timer()
    resultado = funcion(*args)
    fin = timeit.default_timer()
    return fin - inicio, resultado


# Pruebas del programa
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

    # Paso 6
    print("Prueba paso 6")
    print(
        "Revisa si dicho número binario existe dentro la lista de minterminos",
        "[1010,0000,1000,0001]", "1010")
    print(dentro_de_la_lista(["1010", "00-0", "1000", "0001"], "1010"))
    print(
        "Revisa si dicho número binario existe dentro la lista de minterminos",
        "[1010,0000,1000,0001]", "0010")
    print(dentro_de_la_lista(["1010", "0000", "1000", "0001"], "0010"), "\n\n")

    # Prueba Quine McCluskey
    print("----Prueba de  Quine McCluskey----")
    print("Entrada:", 4, [1, 4, 6, 15])
    lista_minterminos = quine_mc_cluskey(4, [1, 4, 6, 15])
    print("Resultado:", lista_minterminos, "\n")

    # Calcular tiempo del algoritmo
    print("Tiempo de ejecucion: ",
          calcula_tiempo(quine_mc_cluskey, 4, [1, 4, 6, 15])[0], "[s]", "\n")

    # Imprime el resultado en forma funcion booleana
    print("Representacion funcional booleana")
    print(obtenga_funcion(lista_minterminos), "\n")


if __name__ == "__main__":
    prueba()
