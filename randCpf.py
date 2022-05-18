from random import randint

def validaCPF(rang, calc, cpf):
    x = 0
    for i in range(0,rang):
        x += int(cpf[i]) * calc
        calc-=1
        
    x = 0 if ( 11 - (x % 11) > 9) else (11 - (x % 11))
    return str(x)

def criaCpf():
    return str(randint(10000000000, 99999999999))

while True:
    cpf = criaCpf()
    cpfVali = cpf[:9]
    cpfVali += validaCPF(9, 10, cpf[:9])
    cpfVali += validaCPF(10, 11, cpf[:10])
    if (cpf == cpfVali):
        break;

print(f'CPF = {cpf}')