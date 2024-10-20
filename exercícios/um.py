def recebe_base():
    salario = float(input('Qual o seu salário?'))
    aumento = float(input('Qual foi o valor do aumento?'))
    return salario, aumento
def calcula_aumento(salario, aumento):
    valor_final = salario+(salario*(aumento/100))
    print(f'O valor final é de {valor_final}')

salario, aumento = recebe_base()
calcula_aumento(salario,aumento)

