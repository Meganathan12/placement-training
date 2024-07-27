def pascal(x):
    
    for i in range(1,x+1):
        for j in range(0,x-i+1):
            print(" ",end="")
        y=1
        for j in range(1,i+1):
            print(" ",y,sep="",end="")

            y=y*(i-j)//j
        print()

x=int(input("Enter the number :"))
pascal(x)
