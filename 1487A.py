'''
https://codeforces.com/problemset/problem/1487/A
Solution: All players which have a higher level from the weakest player(s) in the 
group can win at least one game. Hence we need find the minimum level for a player
and count how many of those are present. All the remaining players are potential
winners. 
'''
from array import *
def solve(n, arr):
    min_elem = min(arr)

    min_elem_freq = 0
    for a in arr:
        if a == min_elem:
            min_elem_freq += 1

    return (n - min_elem_freq)


if __name__ == "__main__":

    t = int(input())

    for _ in range(0, t):
        n = int(input())
        arr = array('i',list(map(int, input().rstrip().split())))
        print(solve(n, arr))

         