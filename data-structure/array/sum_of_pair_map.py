
def main1(list1,sum):
    pairs=[]
    for i in list1:
        #print(i,17-i)
        pairs.append([i,17-i])
    print(pairs)
    for i in pairs:
        #print(i)
        print(set(i))
        if set(i).issubset(list1):
            print(i)


if __name__=="__main__":
    list1=[1,11,3,5,6,7,8]
    main1(list1,12)

