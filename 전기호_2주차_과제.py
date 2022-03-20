# 문제 1번
def sum(a,b):
    #
    return(a+b)

# 문제 2번
def sub(a,b):
    # your 
    return (a-b)

# 문제 3번
def mul(a,b):
    # your code
    return(a*b)

# 문제 4번
def div(a,b):
    # your code
    return(a/b)

# 문제 5번
def distance(x1,y1,x2,y2):
    # your code typeerror unsupported~~str int
    cal1=(x1-x2)**2
    cal2=(y1-y2)**2

    return (cal1+cal2)**(1/2)

# 문제 6번 나중에 하자
def short():
    lylic = "life is short art is long"
    
    return lylic[8:13:1]


# 문제 7번 몰라
def myReverse(string):
    # your code
    return string[::-1]

# 문제 8번
def letMeIntroduceMyself():
    이름=input("이름이 뭐에요?")
    취미=input("취미가 뭐에요")
    대학=input("대학 어디다니나요?")
    생일=input("언제 태어났어요?(예시:020429)")

    self = ("제 이름은 %s입니다. 제 취미는 %s이구요. 저는 %s를 다니고 있습니다. 제 생일은 %s월%s일 입니다!"%(이름,취미,대학,생일[2:4],생일[4:6]))
    return self


# 문제 9번
def calcAI():
    # your code
    c1=input("첫번째 숫자를 입력하시오")
    c2=input("두번째 숫자를 입력하시오")
    int(c1)
    int(c2)
    result=int(c1)+int(c2)
    return ("두 수의 합은 %d입니다"%result)


