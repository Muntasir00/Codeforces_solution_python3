'''
https://codeforces.com/problemset/problem/615/A
Solution: All about implementation. Create an array for m bulbs. As we get the bulb-indices that are turned on my a 
particular switch, set them 1 denoting turned on. After all the input as been fed in this array, check if there is still
a bulb set as off (as 0), and return NO then. If none found, return YES. 
'''
def solve(bulbs):
    for bulb in bulbs:
        if bulb == 0:
            return "NO"
    return "YES"

if __name__ == '__main__':
    n,m = map(int,input().split(" "))
    bulbs = [0]*m #array sized for m bulbs
    for _n in range(0, n):
        vals =list(map(int, input().split(" ")))
        vals.pop(0)
        for bulbIdx in vals:
            bulbs[bulbIdx-1] = 1 ##-1 since bulb numbers are indexed from 1, opposed to 0 in arrays
    print(solve(bulbs))   
        
    