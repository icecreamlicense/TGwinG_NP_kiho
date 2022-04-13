import math


def calcCircleArea(r):
    result = float()
    
    
    result= format((float(r)**2)*math.pi,".2f")
    '''[2]'''
    return result


def calcLog(a, b):
    result = float()
    '''[3]'''
    
    result=format(math.log(b,a),".2f")
    return result


def calcSin(x):
    result = float()
    '''[4]'''
    
    result=format(math.sin(x),".2f")
    return result

def calcFactorial(x):
    result = int()
    result= math.factorial(5)
    '''[5]'''
    
    return result


def calcCombination(n, r):
    result = int()
    result =math.comb(n,r)
    '''[6]'''

    return result

def calculator(order):
    answer=0
    '''[1]'''
    a=order.split()

    
       
    if a[0]=="원넓이:":
        answer= calcCircleArea(a[1])
    elif a[0]=="로그:":
         if a[1]=="e":
             a[1]=math.e
             answer= calcLog(float(a[1]),float(a[2]))
         elif a[2]=="e":
              a[2]=math.e
              answer= calcLog(float(a[1],float(a[2])))
         else:  
          answer= calcLog(float(a[1]),float(a[2])) 
    elif a[0]=="사인:":
         answer=calcSin(float(a[1]))
    elif a[0]=="팩토리얼:":
        answer= calcFactorial(int(a[1]))
    elif a[0]=="조합:":
        answer=calcCombination(int(a[1]),int(a[2]))
    else: answer="명령어가 없습니다"
    return answer

    



print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 5 2"))

print(math.e)
