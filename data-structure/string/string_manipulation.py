
def main():
    string="himanshu pant"
    substring="pant"

    if substring in string:
        print(f"{substring} found")
    else:
        print("Not found")
        print(set(substring))


    if string.find(substring)!=-1:
        print("found again")

    else:
        print("Not found")



if __name__=="__main__":
    main()
