
def rec_sum(num):
    if num==1:
        return 1
    else:
        return num+rec_sum(num-1)

def digit_sum(num):
    sum = 0
    while num:

        rem=num%10
        sum+=rem
        num=int(num/10)
    return sum


def digit_sum_rec(num):
    sum=0
    if num==0:
        return 0
    else:
        return num%10+digit_sum_rec(int(num/10))








if __name__=="__main__":
    print(rec_sum(4))
    print(digit_sum(4321))
    print(digit_sum_rec(4321))