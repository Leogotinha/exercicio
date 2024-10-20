def DivisaoError():
    try:
        primeiro_valor = int(input('Insira um valor'))
        segundo_valor = int(input('Insira um valor'))
        print(f'O resultado foi{primeiro_valor/segundo_valor}')
    except ZeroDivisionError:
        print('ERRO: não é possível dividir por zero!')
    except ValueError:
        print('ERRO: caractére não válido!')

def ler_arquivo():
    try:
        with open("dados.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print('Esse arquivo não foi encontrado!!')

def entrada_idade():
    try:
        idade = int(input('Digite sua idade: '))
        print(f'Você tem {idade} anos')
    except Exception:
        print('Algo deu errado. Verifique a entrada')

def divisao_finally():
    try:
        primeiro_valor = int(input('Insira um valor'))
        segundo_valor = int(input('Insira um valor'))
        print(f'O resultado foi{primeiro_valor/segundo_valor}')
    except ZeroDivisionError:
        print('ERRO: não é possível dividir por zero!')
    finally:
        print('Operação finalizada')
divisao_finally()