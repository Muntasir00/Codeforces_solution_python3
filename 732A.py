'''
https://codeforces.com/problemset/problem/732/A
Solution: Generate the multiples of k. Those should either be directly divisible by 10 or should have a remainder
equal to the coin value (r). 
'''
def solve(k,r):
    possible_ramainders = {0, r}
    i = 1 
    while True:
        mod = (i*k) % 10 
        if mod in possible_ramainders:
            return i  
        else:
            i+=1 

if __name__ == '__main__':
    k,r = map(int, input().split(" "))
    print(solve(k,r))  