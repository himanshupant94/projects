


def peak_element(arr):
    index=0
    maximum=0
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
            index=i
    print(arr[index])
    return index


if __name__=="__main__":
    arr=[4,56,3,6,36]
    print(max(arr))
    print(peak_element(arr))