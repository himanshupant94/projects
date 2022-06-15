

def reverse_string(str):
    #print(len(str.strip()))
    print(str.split())

    print(" ".join(str.split()[::-1]))  # slicing to reverse list
    # reversed function to reverse list,tuple,string and use list function to make list
    return " ".join((reversed(str.split())))


if __name__=="__main__":
    str=" my name is himanshu pant "
    print(reverse_string(str))