print('Analizador de tipos primitivos - 2018')
caixa = input('Digite o dado para ser analisado: ')
print('O tipo de dado é?', type(caixa))
print('Ele é alphanumerico? :',caixa.isalpha())
print('Ele é numerico?: ',caixa.isnumeric())
print('Ele é um decimal? :',caixa.isdecimal())
print('Ele é um espaço? :',caixa.isspace())