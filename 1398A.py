'''
https://codeforces.com/problemset/problem/1398/A
Solution: By triangle inequality, any two sides should sum to be >= third side. Since tha given array is sorted in 
non-decreasing order, the smallest two values in it would be the first and second element, while the largest is the
last element. If the inequality of first + second > last satisfied, then there doesn't exist any triplet that can
produce the required non-degenerate invalid triangle). Hence we return -1. If not, a possible way to construct the non-
degenerate invalid triangle is via sides at 0th, 1st and n-1th indices. We return them in 1-indexed form.  
'''
def solve(n, arr):
    if arr[0] + arr[1] > arr[n-1]:
        return -1
    else:
        return "1 2 "+str(n)
    
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        arr = list(map(int, input().rstrip().split(" ")))
        print(solve(n, arr))
        
         