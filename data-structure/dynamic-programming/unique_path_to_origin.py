

def count_path(n,m):
    if (n==0 or m==0 ):
        return 1
    else:
        return (count_path(n-1, m) + count_path(n, m-1))


if __name__=="__main__":
     x,y=2,2
     print(count_path(x,y))

