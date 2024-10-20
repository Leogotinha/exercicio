def soma_de_numeros_em_lista():
    final = 0
    lista = []
    for b in range(0,5):
        valor = int(input('Digite um número'))
        lista.append(valor)
    for a in range(0,5):
        final +=lista[a]
    total = lista
    #2 métodos para fazer a soma da lista
    final2= sum(total)
    print(f'O valor final foi de {final2}')


def soma_de_numeros_pares_em_lista():
    total = 0
    lista =[1,2,3,4,5,6,7,8,9,10]
    for numero in lista:
            if numero % 2 == 0:  # Verifica se o número é par
                total += numero  # Adiciona ao total se for par
        
    print(total)

def menor_maior():
    resultado = []
    lista = []
    
    for a in range(0,7):
        valor = int(input('Adicione um valor inteiro'))
        lista.append(valor)
    menor = maior = lista[0]
    for a in lista:
        if a > maior:
            maior = a
        if a < menor: 
            menor = a
    resultado.append(maior)
    resultado.append(menor)
    print(resultado)
         
         