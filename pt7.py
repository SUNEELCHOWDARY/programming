n=9
for i in range(1,10,1):
    for j in range(1,10,1):
        if (i+j==n+1-4 or i+j==n+1+4 or i==j-4 or i==j+4):
            print("*",end='')
        else:
            print(" ",end="")
    print("")  
    

              