
def bubble_sort(arr):
   for i in range(len(arr)-1,0,-1):
       for j in range(i):
           if arr[j]>arr[j+1]:
               """temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp"""
               arr[j + 1], arr[j] = arr[j], arr[j + 1]



if __name__=="__main__":
    arr=[4,5,3,2,2,6,7,8,8,4,3]
    bubble_sort(arr)
    print(arr)