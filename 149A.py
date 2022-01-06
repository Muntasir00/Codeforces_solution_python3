'''
Problem Url: http://codeforces.com/problemset/problem/149/A
Algorithm: Sort the list of monthly growth in reverse order. Traverse the list and add monthly growth. In every
iteration track if the count is equal or greater than required growth (k). If so break from the iteration.
While returning the final check, check for it again and return either the count of months or -1 accordingly.
'''
def solve(k, i_list):
    k1 = months = 0
    if k ==0:
        return months 
    i_list.sort(reverse=True)
    for i in i_list: 
        if k1 >= k:
            break
        else: 
            k1 += i
            months +=1
    if k1 >= k:
        return months 
    else:
        return -1
    
if __name__ == '__main__':
    k = int(input())
    i_list = list(map(int, input().rstrip().split()))
    print(solve(k,i_list))   