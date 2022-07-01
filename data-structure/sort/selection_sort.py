def selection_sort(arr):
    for i in range(len(arr)-1):
        min_pos=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min_pos]:
                min_pos=j
        arr[min_pos],arr[i]=arr[i],arr[min_pos]
        print(arr)

if __name__=="__main__":
    arr=[4,5,3,2,6,7,8,4,3]
    selection_sort(arr)
    #print(arr)