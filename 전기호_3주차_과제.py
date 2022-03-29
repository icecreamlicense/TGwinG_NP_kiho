# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    # your code
    return ("next")

# 문제 2번
def leapYear(year):
    # 
    if int(year)%400==0:
        return("윤년입니다")
    elif int(year)%100==0:
       return("윤년이 아닙니다")
    elif int(year)%4==0:
        return("윤년입니다")
    else:
         return("윤년이 아닙니다")


# 문제 3번

time=int

def alram(time):
    a=int(time)//100
    b=int(time)%100
    if a==12 and b>=45:
        return("오후12시%s분"%b-45)
    elif a==12 and b<45:
        return ("오전11시%d분"%b+15)
    elif a==1 and b<45:
        return("오전00시%d분"%b+15)
    elif a>12 and b>=45:
        return ("오후%d시%d분"%(a,b-45))
    elif a>12 and b<45:
        return ("오후%d시%d분"%(a-1,b+15))
    elif a<12 and b>=45:
        return("오후%d시%d분"%(a,b-45))
    elif a<12 and b<45:
        return("오후%d시%d분"%(a-1,b+15))

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
   d=((x1-x2)**2+(y1-y2)**2)**0.5
   
   if x1==x2 and y2==y1 and r1==r2:
    return("어딘지 모르겠다 오버")
   elif d==r1+r2 or r1==d+r2 or r2==d+r1:
       return(1)
   elif r1>r2 and d<r1+r2 and d+r2>r1:
       return(2)
   elif r2>r1 and d<r1+r2 and d+r1>r2:
       return(2)
   else: return(0)

