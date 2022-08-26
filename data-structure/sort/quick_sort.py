


def quick_sort(arr):

    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    print(mid)
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)

    #print("left:",left)
    #print("right:",right)
    merge_sorted_array_new(left,right,arr)

def merge_sorted_array_new(a,b,arr):

    i,j,k=0,0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1

    while i< len(a):
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1



if __name__=="__main__":
    a=[1,2,3,4,5]
    b=[3,4,5,6,7,8]
    arr=[3,4,6,3,52,3,5,67,3,32,5]
    #merge_sorted_array(a,b)
    quick_sort(arr)
    print(arr)
