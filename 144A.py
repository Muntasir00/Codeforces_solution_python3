'''
https://codeforces.com/problemset/problem/144/A
Solution: Interesting problem.
Firstly, we prefer to get the largest value on the left-most index and smallest value on the right-most index.
This way we reduce the swaps in case of duplicates for largest/smallest values.
Once we have the indices, the no. of swaps needed for the largest value to reach the left most index (0) is its current index.
Similarly, the no. of swaps needed for the smallest value to reach the right most index (n-1) is n - 1 - its current index.
Now if the largest value is right of the smallest value currently, we will do one swap between them too. This should reduce
the swaps count by 1.
Return this swap value as final answer. 
'''
def solve(n,heights):
    maxval = heights[0]
    maxvalindx = 0
    minval = heights[n-1]
    minvalindx = n-1 
    
    for i in range(0, n):
        if heights[i] > maxval:
            maxval = heights[i]
            maxvalindx = i  
        if heights[i] <= minval:
            minval = heights[i]
            minvalindx = i
    swaps = maxvalindx
    swaps += (n-1)-minvalindx
    if maxvalindx > minvalindx:
        swaps -= 1
    
    return swaps
if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().rstrip().split()))
    print(solve(n,heights))