
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

   # Remove blank characters
    print(string.replace(" ",""))
   # Sort string
    print(''.join(sorted(string)).strip())




if __name__=="__main__":
    main()
