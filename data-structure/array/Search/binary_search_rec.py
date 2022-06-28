def binary_search(arr,num):
    if len(arr)==0:
        return False
    else:
        mid=int(len(arr)-1/2)
        #print(mid,arr)
        if arr[mid]==num:
            return True
        else:
            if num<arr[mid]:
                return binary_search(arr[:mid],num)
            else:
                return binary_search(arr[mid+1:],num)




if __name__=="__main__":
    arr=[1,2,3,4,4,5,6,7,7,8,9,10]
    print(binary_search(arr,7))
    #print(result)