#Programa raiz quadrada
var1=float(input(': '))  # type: float
var2=var1
for var3 in range(0,11):
    var4= -((var1-var2**2)/(2*var2))
    var2= var2-var4
print(var2)
