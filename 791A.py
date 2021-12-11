'''
https://codeforces.com/problemset/problem/791/A
Solution: Nothing fancy. Just run a loop till Limak's weight surpasses that of Bob's. Keep incrementing year in every
iteration. 
'''
def solve(l, b):
    years = 0
    while(l<=b):
        l = l*3
        b = b*2
        print(l,b)
        years += 1
    return years  

if __name__ == '__main__':
    l, b = map(int, input().rstrip().split(" "))
    print(solve(l, b))       