n = int(input("n = "))
num = n
len = 0
while(n!=0):
    r=n%10
    n=n//10
    len = len+1
n=num
arm=0
while(n!=0):
    r=n%10
    n=n//10
    arm=arm+r**len

if (arm==num):
    print("its a armstrong")
    
else:
    print("its not an ")            