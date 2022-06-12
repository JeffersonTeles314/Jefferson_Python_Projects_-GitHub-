from random import randint
var1=randint(1,6)
print('---{}---'.format(var1))
if var1==6 or var1==5:
	print('very good')
elif var1==4 or var1==3:
	print('good')
else :
	print('too bad')
