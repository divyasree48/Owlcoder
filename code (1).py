#count set bits
t=int(input())
while(t):
    n=int(input())
    print(bin(n)[2::].count('1'))
    t-=1