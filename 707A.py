'''
https://codeforces.com/problemset/problem/707/A
Solution: Nothing fancy. Just run through the color rows and check in its length if any color is C,M or Y. If so,
its colored. If none of those are found in all colors, its black and white. 
'''
def solve(colors):
    for color in colors:
        for i in range(0, len(color)):
            if color[i] == 'C' or color[i] == 'M' or color[i] == 'Y':
                return "#Color"
    return "#Black&White"

if __name__ == '__main__':
    n,m = map(int,input().split(" "))
    colors = []
    for _n in range(0,n):
        colors.append(input())
    print(solve(colors))