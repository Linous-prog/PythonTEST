n = (input("Digite algo: "))
print('O tipo Primitivo desse valor é ',type(n))
print('só tem espaços? ',n.isspace())
print('É um número? ',n.isnumeric())
print('É alfabético? ',n.isalpha())
print('É alfanumérico? ',n.isalnum())
print('Está em maiúsculas?',n.isupper())
print('Está em minusculas?' ,n.islower())
print('Está capitalizada?',n.istitle())


 # ======================= Ordem de Precedência  ============================
#
# 1-() -Parênteses (para expressões aritiméticas usaremos apenas parênteses)
# 2-** -Potências (exponênciação é a segunda ordem de precedência)
# 3-* / // % - (M,D,DI,RD)
# 4-+ - - Por último faremos as somas e subtração binárias.
#
#
# 		EX: 5 + 3 * 2 = 11
#
# 	Pela ordem de precedência a multiplicação vem antes da soma:
#
#
# 			3 * 2 = 6
# 			6 + 5 = 11
#
#
# 		EX: 3 * 5 + 4 ** 2
#
# 			4 ** 2 = 16
# 			3 * 5 = 15
# 			15 + 16 = 31
#
#
# 		EX: 3 * ( 5 + 4) ** 2
#
# 			5 + 4 = 9
# 			9 ** 2 = 81
# 			81 * 3 = 243
# ============================================================================