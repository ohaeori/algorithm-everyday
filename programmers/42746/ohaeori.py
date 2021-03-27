def solution(num): 
    answer = list(map(str, num)) 
    for i in range(len(answer)):
        if len(answer[i]) <= 3:
            answer[i] = answer[i]*3
    temp = sorted(num,key=lambda x:answer[num.index(x)],reverse=True)
    temp= list(map(str,temp))
    return str(int(''.join(temp)))

def solution2(num): 
    num = list(map(str, num)) 
    answer = sorted(num,key = lambda x:x*3,reverse=True)
    return str(int(''.join(answer)))

solution([3, 30, 34, 5, 9])

