def corta_haste(p, n):
    """Take a list p of prices and the rod length n and return lists r and s.
    r[i] is the maximum revenue that you can get and s[i] is the length of the
    first piece to cut from a rod of length i."""
    # r [i] é o valor máximo para o comprimento da haste i
    # r [i] = -1 significa que r [i] ainda não foi calculado
    r = [-1]*(n + 1)
 
    # s [i] é o comprimento do corte inicial necessário para o comprimento da haste i
    # s [0] não é necessário
    s = [-1]*(n + 1)
 
    corta_haste_helper(p, n, r, s)
 
    return r, s
 
 
def corta_haste_helper(p, n, r, s):
    """Pegue uma lista p de preços, o comprimento da haste n, uma lista r de receitas máximas
    e uma lista de cortes iniciais e retornar a receita máxima que você pode obter
    de uma vara de comprimento n.
 
    Além disso, preencha r e s com base nos subproblemas que precisam ser resolvidos.
    """
    if r[n] >= 0:
        return r[n]
 
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            temp = p[i] + corta_haste_helper(p, n - i, r, s)
            if q < temp:
                q = temp
                s[n] = i
    r[n] = q
 
    return q
 
 
    n = int(input('Digite o comprimento da haste: '))
 
# p[i] é o preço de uma haste de comprimento i
# p[0] não é necessário, por isso está definido None
    p = [None]
    for i in range(1, n + 1):
        preco = input('Entre com o preço de corte da barra {} in: '.format(i))
        p.append(int(preco))
 
    r, s = corta_haste(p, n)
    print('O valor maximo obtido:', r[n])
    print('A haste tem que ser cortada nos compirmento(s) de: ', end='')
    while n > 0:
        print(s[n], end=' ')
        n -= s[n]

