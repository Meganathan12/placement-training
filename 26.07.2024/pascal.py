def pascal(n):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("",end="")
        x=1
        for j in range(1,i+1):
            print("",x,sep="",end="")
            x=x*(i-j)//j
        print()

x=int(input("Entr the number :"))
pascal(x)
