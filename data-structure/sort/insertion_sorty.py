
def insertion_sort(a):
    for i in range(1,len(a)):
        value=a[i]
        j=i-1
        while j>=0:
            if a[j]>value:
                a[j+1]=a[j]
                a[j]=value
                j=j-1
            else:
                break

if __name__=="__main__":
    a=[2,4,42,6,2,5,7,78,1]
    insertion_sort(a)
    print(a)