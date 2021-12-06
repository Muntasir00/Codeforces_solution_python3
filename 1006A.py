'''Here we can solve it with a simple logic.If we see carefully,
odd numbers remains the same but even numbers are reduced by 1'''
from array import *
def solve(n, arr):
    for i in range(0, n):
        if arr[i] % 2 == 0: 
            arr[i] -= 1
    for a in arr:
        print(a)

if __name__ == '__main__':
    n = int(input())
    arr = array('i',list(map(int, input().rstrip().split())))
    solve(n, arr)