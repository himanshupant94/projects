def starPattern(row):

    if row==0:
        return
    else:
        starPattern(row-1)
        print("* "*row)

if __name__=="__main__":
    row=int(input("Rows:"))
    starPattern(row)