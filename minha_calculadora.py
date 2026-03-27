def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    x = int(input('x? '))
    y = int(input('y? '))
    #print(f'Soma da alegria: {soma(x, y)}')
    print(f'Subtração: {subtrai(x, y)}')
    print(f'Multiplicação: {multiplica(x, y)}')
    print(f'Divisão: {divide(x, y)}')

main()