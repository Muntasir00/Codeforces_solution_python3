'''
https://codeforces.com/problemset/problem/1509/A
Solution: Since the adjacent pairs have to sum and be completely divisible by 2 for being most photogenic, the elements
in the pair should both be odd or even (odd + odd and even + even makes an even number). Hence we segregate the array
keeping odds on on end and evens on the other.  
'''
from array import *
def solve(n, arr):
    
    result = [0] * n
    odd_idx = 0
    even_idx = n-1
    for i in range(0, n):
        if arr[i] % 2 == 0:
            result[even_idx] = arr[i]
            even_idx -= 1
        else:
            result[odd_idx] = arr[i]
            odd_idx += 1

    return " ".join(str(_) for _ in result)
            
if __name__ == '__main__':
    t = int(input())
    for _ in range(0,t):
        n=int(input())
        arr =array('i',list(map(int, input().rstrip().split())))
        print(solve(n, arr))
        


