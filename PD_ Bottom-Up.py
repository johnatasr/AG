def corta_haste(p, n):
    """Pega uma lista p de preços e o tamanho da barra n e retornar umas lista r e s.
    r[i] é o valor maximo  que voce pode pegar e s[i] é o tamanho do primeiro 
    pedaço de corte da barra tamanho i."""
    # r[i] é o maximo de valor para a barra de tamanho i
    # r[i] = -1 significa que r[i] nao foi calculado ainda
    r = [-1]*(n + 1)
    r[0] = 0
 
    # s[i] é o tamanho inicial de corte que precisa para a barra de tamanho i
    # s[0] nao é necessario
    s = [-1]*(n + 1)
 
    for i in range(1, n + 1):
        q = -1
        for j in range(1, i + 1):
            temp = p[j] + r[i - j]
            if q < temp:
                q = temp
                s[i] = j
        r[i] = q
 
    return r, s
 
 
    n = int(input('Entre com o tamanho da barra: '))
 
    # p[i] é o preco da barra de uma barra de tamanho i
    # p[0] não é necessario, entao está setado como none
    p = [None]
    for i in range(1, n + 1):
        preco = input('Entre com o preço de corte da barra {} em: '.format(i))
        p.append(int(preco))
 
    r, s = corta_haste(p, n)
    print('O valor maximo obtido:', r[n-1])
    print('A barra precisa ser cortada no(s) tamanho(s) de ', end='')
    while n > 0:
        print(s[n], end=' ')
        n -= s[n]

#1. The user is prompted to enter the length of the rod n.
#2. The user is then asked to enter the price for each length of rod.
#3. cut_rod is called and the lists r and s are returned.
#4. r[n] is the maximum revenue that we can earn from a rod of length n.
#5. The way to cut the rod is determined using s where s[i] tells you the length of the first piece to cut of from a rod of length i. 
#6. So s[n] gives us the length of the first piece, s[n – s[n]] gives us the length of the second piece and so on.
