
def stringinlist(string,word_list):
    output=[]
    for word in word_list:
        if word in string:
            output.append(word)
            string=string.replace(word,"")
            print(string)

    if string:
        return False
    else:
        return True


if __name__=="__main__":
    string="kesariyateraishqhaipiya"
    word_list=["piya","ishq","hai","tera","kesariya"]
    print(stringinlist(string,word_list))
