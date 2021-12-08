'''
http://codeforces.com/problemset/problem/141/A
Solution: Create frequency distribution of each letter in each word by using Counter. Add them to make
their joint distribution. Compare with the similar distribution of the jumbled words.
If they match, return YES. Else return NO.
'''

class AmusingJoke:
    name1 = ""
    name2 = ""
    jumbletters = "" 
    
    def solve(self):
        from collections import Counter
        map1 = Counter(self.name1)
        map2 = Counter(self.name2)
        map_jumltr = Counter(self.jumbletters)
        map_name =Counter(map1+map2)
        if (map_name==map_jumltr):
            return "YES"
        else:
            return "NO"
        
if __name__ == '__main__':
    a = AmusingJoke() 
    a.name1 = input()
    a.name2 = input()
    a.jumbletters = input()
    print(a.solve())  


