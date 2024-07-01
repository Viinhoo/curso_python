try:
    palavra = input('digite algo: ')
    int1 = int(palavra)
    str1 = str(palavra)
    print(type(palavra))
    if " " in palavra:
        print(True)
    elif " " not in palavra:
        print(False)
except ValueError: