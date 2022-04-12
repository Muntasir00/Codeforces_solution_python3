'''
https://codeforces.com/problemset/problem/1223/A
Solution: We need at least need 4 matchsticks to make the equation work (I + I = II). Hence for any value of n 
<= 4 should require n - 4 sticks to make it work. For all others, we make the odd number of match sticks as 
next nearest even so that we can split on LHS and RHS of CME. We need to find next nearest even since we can
only buy sticks, not discard.  
'''
def solve(n):
    if n <= 4:
        return 4-n 
    return n%2 

if __name__ == '__main__':
    t = int(input())
    results = []
    for i in range(0,t):
        n = int(input())
        results.append(solve(n))
    for result in results:
        print(result)
         