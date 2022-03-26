import random as rd
def pwmk(ln):
    lett={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'}
    LETT={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'}
    numb={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    le=set()
    LE=set()
    nu=set()
    all = list(numb|lett|LETT)
    while (len(le) == 0) or (len(LE) == 0) or (len(nu) == 0):
        pw = ''
        le = set()
        LE = set()
        nu = set()
        for i in range(ln):
            pw = pw + rd.choice(all)
        le = {x for x in pw if (x in lett)}
        LE = {x for x in pw if (x in LETT)}
        nu = {x for x in pw if (x in numb)}
    return pw

while True:
    a = int(input('How many characters? '))
    b = pwmk(a)
    print(b)