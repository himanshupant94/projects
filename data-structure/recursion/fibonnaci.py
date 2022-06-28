def fibonaci_iter(num):
    a=0
    b=1
    for i in range(num):
        a,b=b,a+b
        print(a,b)
    return a

def fibonaci_rec(num):
    a,b=0,1
    if num==0 or num==1:
        return num
    else:
        return fibonaci_rec(num-1)+fibonaci_rec(num-2)

def fibonaci_3rd(num):
    a,b=0,1
    c=0
    for i in range(num):
        c=a+b
        a=b
        b=c
    return a





if __name__=="__main__":
    num=5
    #num=int(input())
    print(fibonaci_iter(num))
    #print(fibonaci_rec(num))
    print(fibonaci_3rd(num))
