'''
http://codeforces.com/problemset/problem/431/A
Solution: Iterate over the list of the boxes, add add the calorie for each box entry.
Sum it and return it.
'''

def solve(a, boxes):
    waste = 0 
    for box in boxes:
        waste += a[int(box)-1]
    return waste  
    
if __name__ == '__main__':
    a = list(map(int, input().rstrip().split(" ")))
    boxes = list(map(int, input().rstrip()))
    print(solve(a, boxes))