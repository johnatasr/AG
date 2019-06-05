def corte_haste(p, n):
    r = [-1] * (n + 1)
    s = [-1] * (n + 1)

    corte_haste_helper(p, n, r, s)

    return r, s


def corte_haste_helper(p, n, r, s):
    """Pegue uma lista p de preços, o comprimento da haste n, uma lista r de receitas máximas
    e uma lista de cortes iniciais e retornar a receita máxima que você pode obter
    de uma haste de comprimento n.

    Além disso, preencha r e s com base nos subproblemas que precisam ser resolvidos.
    """
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            temp = p[i] + corte_haste_helper(p, n - i, r, s)
            if q < temp:
                q = temp
                s[n] = i
    r[n] = q

    return q


n = int(input('Entre com o tamanho da haste: '))

p = [None]
for i in range(1, n + 1):
    preco = input('Entre com o preco da haste de tamanho {} no: '.format(i))
    p.append(int(preco))

r, s = corte_haste(p, n)
print('O valor máximo que pode ser obtido:', r[n])
print('A haste precisa ser cortada nos tamanhos: ', end='')
while n > 0:
    print(s[n], end=' ')
    n -= s[n]