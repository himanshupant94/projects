
def finder(arr1,arr2):
    return sum(arr1)-sum(arr2)

if __name__=="__main__":
    arr1=[1,1,2,3,3,4,5]
    arr2=[1,2,1,3,4,5]
    print(finder(arr1,arr2))