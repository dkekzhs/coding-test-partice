def solution(s):
    answer = ''
    s = s.split(" ")
    for i in s:
        for j in range(len(i)):
            if j == 0 :
                answer+= i[j].upper()
            elif j%2 == 0 :
                answer += i[j].upper()
            elif j%2 != 0 :
                answer += i[j].lower()
        answer += " "
    
    return answer[:len(answer)-1]

solution("try hello world")