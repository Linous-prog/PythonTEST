n1 = int(input('Digite um valor: '))
n2 = int(input('Digite Outro valor: '))
r = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
s = n1 - n2
di = n1 // n2
print("A soma vale {}, \nA Divisão é {:.3f}, \nA multiplicação é {:.3f} " .format(r, d, m)) #\n para quebrar a linha e descer(\n=nova linha)
print("A Divisão inteira {} a potência {:.5f}".format(di, e ,), end=' ') #end= ' ' Para continuar o print na tela
print("A subtração {}" .format(s))
