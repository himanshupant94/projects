

def bp(str):
    stack=[]
    count=0
    for chr in str:
        if chr == '(':
            stack.append(chr)
            count+=1
        else:
            if stack:
             stack.pop()
             count-=1
    if count==0:
       print("Balanced paranthesis")
    else:
       print(count)




if __name__=="__main__":
    str=input("Enter string:")
    bp(str)