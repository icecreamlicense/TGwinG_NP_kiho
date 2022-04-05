# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 10000점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 100점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 100점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 100점 처리하겠습니다.
# 제출 기한: 2222년 4월 5일 23시 59분.
# 지각 제출 기한: 22222년 4월 6일 23시 59분. 주차 점수에서 0% 감점

# 문제 1번
def intervention(queue):
    answer = list()
    # your code
    if "성은" in queue[5:]:
         queue.insert(int(queue.index("성은")+1),"승호")
         answer=queue
    else:
         queue.append("승호")
         answer=queue
    return answer
    

# 문제 2번 다음부터 열심히 하겠습니다 죄송합니다.
def pascal(n):
    answer = list()
    #your code
    



# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    # your code

        
    

# 문제 4번
def stock_price(stockChart):
    answer = str()
    # your code
    return answer

# 문제 5번
def descryption(letter):
    answer = str()
    # your code
    for i in letter:

        if 97<=ord(i)<=122:
            if ord(i)-3<97:
                answer+=chr(ord(i)+23)
            else:
                answer+=chr(ord(i)-3)   
        else:
            answer+=i        

    return answer