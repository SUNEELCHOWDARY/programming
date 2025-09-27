n=int(input("n: "))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        if i%2 == 0:
            print("0 ",end='')
        else:
            print("1 ",end='')
    print("") 
    

n=int(input("n: "))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        if (i+j)%2==0 :
            print("1 ",end="")
        else:
            print("0 ",end="")    
    print("")        
    
n = 1
for i in range(1, i + 1,1):
    for j in range(1,i+1,1):
        print(n * n, end=" ")
        n += 1
    print() 