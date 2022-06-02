def isAnagram(str1,str2):
    if sorted(str1.lower())==sorted(str2.lower()):
        return True
    else: return False


if __name__=='__main__':
    str1=input("string 1:")
    str2=input("string 2:")
    print(isAnagram(str1,str2))