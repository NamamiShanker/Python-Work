def fun(search,pattern):
    s_len=len(search)
    p_len=len(pattern)
    ans=1000000000
    for i in range(s_len):
        if search[i]==pattern[0]:
            k=0
            j=i
            while(j<s_len):
                if k==p_len:
                    break
                if search[j]==pattern[k]:
                    k+=1
                j+=1
            if k==p_len:
                
                ans=min(ans,(j-i))
    if ans==1000000000:
        return "NO"
    else:
        return "YES "+str(ans-p_len)

if __name__=="__main__":
    for _ in range(int(input())):
        s,p=input().split()
        print(fun(s,p))
