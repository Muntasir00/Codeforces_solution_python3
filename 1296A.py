'''
https://codeforces.com/problemset/problem/1296/A
Solution: The question boils down to counting evens and odds in the array. If there are no odds, then the sum 
cannot be made odd. Also, if all the numbers are odd and their quantity is even, they will add up to make even
sum. Apart from these two conditions, we can always make sum odd with/without substitution
'''
from array import *
def solve(n,arr):
    even = odd = 0
    for i in range(0, n):
        if arr[i]%2 == 0:
            even += 1 
        else:
            odd += 1
    if odd == 0 or (even == 0 and odd%2 == 0):
        return "NO"
    else:
        return "YES"
    
if __name__ == '__main__': 
    t = int(input())
    for i in range(0, t):
        n = int(input())
        arr = array('i',list(map(int,input().rstrip().split())))
        print(solve(n,arr)) 