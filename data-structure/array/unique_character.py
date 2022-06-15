
def unique_character(str):
    #print(len(set(str))==len(str))
    s=set()
    for i in str:
        if i in s:
            s.add(i)

            return False
        else:
            s.add(i)
    return True

if __name__=="__main__":
    str="abccde"
    print(unique_character(str))