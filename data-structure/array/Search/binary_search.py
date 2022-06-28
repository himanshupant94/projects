

def binary_search(arr,num):
    first=0
    last=len(arr)-1
    found=False

    while first<=last and not found:
        mid=int((first+last)/2)
        if arr[mid]==num:
            found=True
        else:
            if num<=arr[mid]:
                last=mid-1
            else:
                first=mid+1
    return found





if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,9]
    num=9
    print(binary_search(arr,num))