num_var = 0


def entero_a_bin(num_entero):
    global num_var
    return format(num_entero, "0" + str(num_var) + "b")


if __name__ == "__main__":
    num_var = 8
    print(entero_a_bin(18))
