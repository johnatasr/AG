
  


print("--------------------------------------------------------------------------------")


def MaxAtividades(s, f ):
    n = len(f) 
    print("As seguintes atividades são selecionadas:")
  
    # A primeira atividade sempre é selecionada
    i = 0
    print(i)
    
    # Considere o resto das atividades
    for j in range(n): 
  
        # Se essa atividade tem um começo maior que
        # ou igual o final de tempo anterior
        # da atividade selecionada, entao selecione ela
        if s[j] >= f[i]: 
            print(j) 
            i = j


  
    # Testes
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

s = [1, 3, 0, 5, 6]
f = [4, 5, 6, 7, 9]

MaxAtividades(s, f)
  

