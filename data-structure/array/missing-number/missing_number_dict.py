
import collections

def finder(arr1,arr2):
    #arr1=sorted(arr1)
    #arr2=sorted(arr2)
    d=collections.defaultdict(int)
    for num in arr2:
        d[num]+=1
    for num in arr1:
        if d[num]==0:
            return num

        else:
            d[num]-=1






if __name__=="__main__":
    arr1=[1,1,2,3,3,4,5]
    arr2=[1,2,1,3,4,5]
    print(finder(arr1,arr2))