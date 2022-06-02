
def isBalanced(str):
    stack=[]
    dic={'}':'{',']':'[',')':'('}
    for chr in str:
        if chr in dic.values():
            stack.append(chr)
        elif stack and dic[chr]==stack[-1]:
            stack.pop()
        else:
            return False

    if stack:
        return False
    else: return True


# return stack==[]


if __name__=="__main__":
    str="{{}[]()}}"
    print(isBalanced(str))


