import random


def pre_codificacao(msg):
    msg_pre_codificada = []
    for i in msg:
        msg_pre_codificada.append(ord(i))
    return msg_pre_codificada


def gera_num_primo():
    while True:
        n = random.randrange(1, 100)
        cont = 0
        for i in range(1, n+1):
            if n % i == 0:
                cont = cont + 1
        if cont == 2:
            return n


def gera_n(P, Q):
    return P * Q


def gera_z(P, Q):
    return (P-1) * (Q-1)


def gera_e(num):
    # calcula mdc
    def mdc(n1, n2):
        rest = 1
        while(n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1
    while True:
        e = random.randrange(2, num)
        if(mdc(num, e) == 1):
            return e


def cifra_mensagem(msg, E, N):
    mensagem_cifrada = []
    for i in msg:
        mensagem_cifrada.append((i**E) % N)
    return mensagem_cifrada


def gera_d(E, Z):
    D = 1
    while True:
        calculo1 = D * E
        if calculo1 % Z == 1:
            return D
        else:
            D = D + 1


def decrifra_mensagem(msg_cifrada, D, N):
    mensagem_decifrada = []
    for i in msg_cifrada:
        mensagem_decifrada.append(chr((i ** D) % N))
    return mensagem_decifrada


msg = input('Entre com mensagem: ')
msg_pc = pre_codificacao(msg)
P = gera_num_primo()
Q = gera_num_primo()
N = gera_n(P, Q)
Z = gera_z(P, Q)
E = gera_e(Z)
D = gera_d(E, Z)

msg_cifrada = cifra_mensagem(msg_pc, E, N)
msg_decifrada = decrifra_mensagem(msg_cifrada, D, N)

print(f'Mensagem digitada: {msg}')
print(f'Mensagem pré codificada {msg_pc}')
print(f'Chave publica:  {N} e {E}')
print(f'Mensagem cifrada: {msg_cifrada}')
print(f'Chave privada: {D}')
print(f'Mensagem original: {msg_decifrada}')
