#アルファベット
al=[chr(ord('a') + i) for i in range(26)]
print(al)

#素因数分解
pf={}
m=341555136
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pf[i]=pf.get(i,0)+1
        m//=i
if m>1:pf[m]=1
print(pf)

#複数の文字列を変換
S='54IZSB'
S = S.translate(str.maketrans("ODIZSB","001258"))
print(S)

#しゃくとり
n=int(input())
a=list(map(int, input().split()))

count=0
right=0
m=dict()
for left in range(n):
    while right<n and m.get(a[right],0)==0:
        m[a[right]]=m.get(a[right],0)+1
        right+=1
    count=max(count,right-left)
    m[a[left]]=m.get(a[left],1)-1
print(count)
