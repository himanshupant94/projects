

def is_Anagram(s1,s2):

    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    d={}
    if len(s1)!=len(s2):
        return False

    for ch in s1:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1

    for ch in s2:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]-=1
    for k in d:
        if d[k]!=0:
            return False
    return True








s1="himanshu apnt"
s2="himanshu pQnt"
print(is_Anagram(s1,s2))