#__author__ = 'Muntasir Mamun'
#problem "https://codeforces.com/problemset/problem/1311/A"
#in this problem ,let us consider three scenerio
#if difference is 0, result = 0
'''if b > a,diff>0 and we can add only odd number,so if difference is odd result = 1 and
if even then first add(a,1) then add remaining odd number result=2'''
'''if b < a,diff>0 and we can subtrack only even number,so if difference is even result = 1 
and if odd then first subtract(a,(diff+1) then add 1 result=2 '''

def solve(a, b):
    diff = b - a
    if diff == 0:
        return diff
    elif diff > 0:
        if diff % 2 == 0:
            return 2
        else:
            return 1
    else:
        if diff % 2 == 0: 
            return 1 
        else:
            return 2 
        
if __name__ == '__main__':
    t = int(input())
    
    for i in range(0, t): 
        a, b = map(int, input().split(" "))
        print(solve(a, b))
 