
def WordSplit(strArr):
    for i in range(1,len(strArr)-1):
        for j in range(0, len(strArr[0])-1):
            if strArr[0][:j] in strArr[i]:
                print(strArr[0][:j])
        

print(WordSplit(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
  

