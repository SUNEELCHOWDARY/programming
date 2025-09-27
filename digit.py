n=int(input("n: "))
sum=0
prod=1
while(n!=0):
    r=n%10
    n=n//10  
    sum=sum+r
    prod=prod*r
print(sum) 
print(prod)

n=int(input("n: "))
rev = 0
while (n !=0):
    r=n%10
    n=n//10
    rev = rev*10+r
print(rev) 


n=int(input("n: "))
num=n
rev = 0
while (n !=0):
    r=n%10
    n=n//10
    rev = rev*10+r

if num==rev:
    print("its a palindrome")
else:
    print("not")       
    


   