'''
https://codeforces.com/problemset/problem/1326/A
Solution: This is more of a knowledge question. To ensure that non-divisibility with the digits is 
maintained, we generate a number of the form 23...3. This kind of number is not even (hence not
divisible by 2) and the sum of digits would never be divisible by 3 (due to the 2 as the first digit).
The only outlier is when n = 1, when there is no answer.
'''
def solve(n):
    if n == 1:
        return -1
    else:
        return "2" + "3"*(n-1)
    
if __name__ == '__main__':
    t =int(input())
    for i in range(0, t):
        n = int(input())
        print(solve(n))