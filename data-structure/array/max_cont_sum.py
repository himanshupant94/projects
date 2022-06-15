

def max_large_sum(arr):
    if len(arr)==0:
        return 0

    current_sum=max_sum=arr[0]
    for i in arr[1:]:
        current_sum=max(i+current_sum,i)
        max_sum=max(current_sum,max_sum)

    return max_sum





if __name__=="__main__":
    arr=[1,2,-1,2,3,4,7,-6,-1]
    print(max_large_sum(arr))