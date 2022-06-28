def sequential_search_unordered(unordered,num):
    pos=0

    while pos<len(unordered):
        if unordered[pos]==num:
            return True
        else:
            pos+=1
    return False


def sequential_search_ordered(ordered,num):
    found=False
    pos=0
    stop=False

    while pos<len(ordered) and not found and not stop:

        if ordered[pos]==num:
            found=True
        else:
            if ordered[pos]>num:
                stop=True
            else:
                pos+=1

    return found


if __name__=="__main__":
    unordered=[3,6,7,2,5,34,12]
    ordered=[1,2,3,4,5,6,7,8]
    print(sequential_search_unordered(unordered,1))
    print(sequential_search_ordered(ordered,2))
 