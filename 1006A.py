'''Here we can solve it with a simple logic.If we see carefully,
odd numbers remains the same but even numbers are reduced by 1'''
from array import array
def solve(n, arr):
    for i in range(0, n):
        if arr[i] % 2 == 0: 
            arr[i] -= 1
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(solve(n, arr))