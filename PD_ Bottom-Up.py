def cut_rod(p, n):
    """Take a list p of prices and the rod length n and return lists r and s.
    r[i] is the maximum revenue that you can get and s[i] is the length of the
    first piece to cut from a rod of length i."""
    # r[i] is the maximum revenue for rod length i
    # r[i] = -1 means that r[i] has not been calculated yet
    r = [-1]*(n + 1)
    r[0] = 0
 
    # s[i] is the length of the initial cut needed for rod length i
    # s[0] is not needed
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
 
 
n = int(input('Enter the length of the rod in inches: '))
 
# p[i] is the price of a rod of length i
# p[0] is not needed, so it is set to None
p = [None]
for i in range(1, n + 1):
    price = input('Enter the price of a rod of length {} in: '.format(i))
    p.append(int(price))
 
r, s = cut_rod(p, n)
print('The maximum revenue that can be obtained:', r[n])
print('The rod needs to be cut into length(s) of ', end='')
while n > 0:
    print(s[n], end=' ')
    n -= s[n]

#1. The user is prompted to enter the length of the rod n.
#2. The user is then asked to enter the price for each length of rod.
#3. cut_rod is called and the lists r and s are returned.
#4. r[n] is the maximum revenue that we can earn from a rod of length n.
#5. The way to cut the rod is determined using s where s[i] tells you the length of the first piece to cut of from a rod of length i.
#6. So s[n] gives us the length of the first piece, s[n – s[n]] gives us the length of the second piece and so on.
