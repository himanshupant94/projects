

def reverse_rec(string):
    if len(string)<=1:
        return string
    else:
        return reverse_rec(string[1:])+string[0]


if __name__=="__main__":
    string="himanshu pant"
    print(reverse_rec(string))