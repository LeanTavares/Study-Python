from curses.ascii import isalpha


def leiaDinheiro(msg):
    valid = False
    while not valid:
        inp = str(input(msg)).replace(',', '.').strip()
        if inp.isalpha():
            print(f'ERRO: \"{inp}\" is not a valid')
        else:
            valid = True
            return float (inp)
        