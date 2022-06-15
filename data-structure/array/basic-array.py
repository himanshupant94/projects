import array

class Array:
    def array_operation(arr):
        arr.append(8)
        arr.insert(2,3)
        arr.remove(7) # remove first occurance of 7
        arr.pop(-1) # delete last element from array
        arr.pop(0) # delete element from index 0
        print("Index of 2:",arr.index(2)) # index of 2

        arr.reverse()

        for i in range(len(arr)):
            print(arr[i],"\n")





if __name__=="__main__":
    arr=array.array("i",[1,2,4,5,6,7,7])
    Array.array_operation(arr)
