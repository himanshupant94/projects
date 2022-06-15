
def string_compression(string):
    string_compressed=""
    count=1
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1
        else:
            string_compressed+=string[i]+str(count)
            count=1
    print(i)
    string_compressed+=string[i+1]+str(count)
    print(string_compressed)


if __name__=="__main__":
    string="abbccddeeeff"
    string_compression(string)