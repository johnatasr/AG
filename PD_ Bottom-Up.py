def corte_haste(p, n):
    """Pegue uma lista p de preços e o comprimento da haste n e retorne as listas r e s.
    r [i] é a receita máxima que você pode obter e s [i] é o comprimento do
    primeira peça para cortar de uma haste de comprimento i."""
    # r[i] é o valor maximo para a haste temanho i
    # r[i] =  se -1 significa que r[1] nao foi calculado
    r = [-1] * (n + 1)
    r[0] = 0

    # s[i] é o tamanho inicial de corte da haste tamanho i
    # s[0] näo precisa
    s = [-1] * (n + 1)

    for i in range(1, n + 1):
        q = -1
        for j in range(1, i + 1):
            temp = p[j] + r[i - j]
            if q < temp:
                q = temp
                s[i] = j
        r[i] = q

    return r, s


n = int(input('Entre com o tamanho da haste: '))

# p[i] é o preco de uma haste tamanho i
# p[0] náo precisa logo seto none
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