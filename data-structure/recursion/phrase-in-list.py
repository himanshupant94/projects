
def stringinlist(string,word_list,output=None):
    if output is None:
        output=[]

    for word in word_list:
        if string.startswith(word):
            output.append(word)
            print (output)
            stringinlist(string[len(word):],word_list,output)

    return output


if __name__=="__main__":
    string="kesariyateraishqhaipiya"
    word_list=["piya","ishq","hai","tera","kesariya"]
    print(stringinlist(string,word_list,output=None))
