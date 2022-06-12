#Progeto de contrução de programa capaz de gerar raizes quadradas
numraiz = (float(input('por favor insira seu o número desejado aqui: '))
var1 = numraiz
var2 = float(-(numraiz-var1**2)/(2*var1))
var1 = var1-var2
assert isinstance(var1, object)
print(var1)