#top-down

INF = 100000;
r = [0] + [-1*INF]*5

def max(x, y):
  if x > y:
    return x
  return y

def corta_haste(c, n):
  global r
  if(r[n] >= 0):
    return r[n]

  max_valor = -1*INF

  for i in range(1, n+1):
    max_valor = max(max_valor, c[i] + corta_haste(c, n-i))

  r[n] = max_valor
  return r[n]

if __name__ == '__main__':

  c = [0, 1, 15, 3, 5]
  frase = "A melhor escolha é: "
  print(frase)
  print(corta_haste(c, 4))