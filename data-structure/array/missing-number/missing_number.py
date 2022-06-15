


def finder(arr1,arr2):
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    print(tuple(zip(arr1,arr2)))
    for num1,num2 in zip(arr1,arr2): # (1,1),(1,1),(2,2),(3),(
        if num1!=num2:
            return num1





if __name__=="__main__":
    arr1=[1,1,2,3,4,5]
    arr2=[1,2,1,4,5]
    print(finder(arr1,arr2))