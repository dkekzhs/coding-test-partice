def solution(array, commands):
    answer = []

    for i in commands:
        a = array[i[0] -1 :i[1]]
        a.sort()
        b = a[i[2] -1 : i[2]]
        answer.extend(b)
    return answer
    
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])