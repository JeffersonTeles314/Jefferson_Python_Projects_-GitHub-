def andgate(input1, input2):
   if input1==input2 and input1==True :
        return True
   else:
        return False

def orgate(input1, input2):
   if input1==True or input2==True :
        return True
   else:
        return False

def notgate(input1):
   if input1==True :
        return False
   else:
        return True

def xorgate(input1, input2):
   if input1==True and input2==True :
        return False
   elif input1==False and input2==True :
        return True
   elif input1 == True and input2 == False:
        return True
   else:
        return False

def halfadd(input1, input2):
    if xorgate(input1, input2)==True:
       andgate(input1, input2) == True:

def fulladd(input1, input2, input3):