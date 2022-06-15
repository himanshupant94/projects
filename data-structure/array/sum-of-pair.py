
def main(list,sum):
    cnt=0
    for i in range(len(list)):
        #for j in range(len(list)):# It will give all combination of pairs like 11,1 and 1,11
        for j in range(i,len(list)):  # It will not give duplicate pair
            if list[i]+list[j]==sum:
                print(list[i],list[j])
            cnt += 1
    return cnt

def sumOfPair(list,sum):
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i]+list[j]==sum:
                print(list[i],list[j])





if __name__=="__main__":
    list=[1,11,3,5,6,7,8]
    count=main(list,12)
    print(count)
