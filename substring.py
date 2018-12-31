def substring(str,n):
    for le in range(1,n+1):
        for i in range(0,n-le+1):
            j=i+le-1
            b = ["\0"]
            for k in range(i,j+1):
                print(str[k],end="")
            print("\n")
t=input()
for i in range(int(t)):
    s=input()
    substring(s,int(len(s)))



