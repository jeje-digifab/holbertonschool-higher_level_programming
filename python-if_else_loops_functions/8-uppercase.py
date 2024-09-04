def uppercase(str):
    """
    Convertit toutes les lettres minuscules d'une chaîne
    en majuscules et imprime le résultat.

    Args:
        str (str): La chaîne d'entrée à convertir.

    Returns:
        None
    """

    for letter in str:
        if letter >= "a" and letter <= "z":
            new_str = (ord(letter)) - 32
        else:
            new_str = (ord(letter))

        print("{}".format(chr(new_str)), end="")

    print()
