#__author__ = 'Muntasir Mamun'

'''
https://codeforces.com/problemset/problem/1354/A
TODO
Solution: 
'''
'''here description is little bit complex.Polycarp needs a minutes sleep,but he wakes up after d minutes,so if a<=b 
thats means his required time of sleep is fulfilled,ans will be b.If a > b then he requires a-b minutes sleep.As he sets his 
alarm after c minutes and he requires d minutes to fall asleep,if c > d,he never fall asleep again,ans will be -1 . If c<=d
then he can sleep for c-d minutes.And ans will be gained by below equation.
'''

import math  
def solve(a, b, c, d):
    if a <= b:
        return b
    elif c <= d:
        return -1 
    else:
        sleep_needed = a-b
        inter_alarm_sleep = c-d 
        sleep_segment_needed  = math.ceil(float(sleep_needed)/float(inter_alarm_sleep))
        return int(sleep_segment_needed*c) + b 
    
if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        a, b, c, d = list(map(int, input().rstrip().split()))
        print(solve(a, b, c,d))
   