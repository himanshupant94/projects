

def reverse_string(str):
    str=str.strip()
    result=[]
    new_result=[]
    length=len(str)
    i=0
    while i < length:
        if str[i] != " ":
            start_word=i
            while i< length and str[i]!=" ":
                i+=1
            result.append(str[start_word:i])
        i+=1
    print(result)
    for i in range(len(result)-1,-1,-1):
        new_result.append(result[i])
    return (" ".join(new_result))









if __name__=="__main__":
    str=" my name is himanshu pant "
    print(reverse_string(str))

