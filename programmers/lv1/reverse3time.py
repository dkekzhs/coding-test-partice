def solution(s):
    t = ''
    while s >0 :
        s,r  = divmod(s,3)
        t += str(r)
    
   
    return int(t,3)

solution(45)