
def shell_sort(a):
    gap=len(a)//2 #4
    while gap>0:
        for i in range(gap,len(a)):
            value=a[i]
            j=i
            while j>=gap and a[j-gap]>value:
                a[j]=a[j-gap]
                j=j-gap
            a[j]=value
        gap=gap//2

if __name__=="__main__":
    a=[2,4,42,6,2,5,7,78,1]
    shell_sort(a)
    print(a)