import sys

# sys.set_int_max_str_digits(1000000)

while(True):
    match input("0-INFO \n1-find Lychrel numbers \n2-test your number \n"):
        case "0":
            print("-- nothing here --\nbut notice in mode 1 after every Lychrel number you should press ENTER to continue \nIf you want to leave press ctrl + c")
            input("\n")
        case "1":
            startNum=0
            while(True):

                num = str(startNum)
                iteration=0
                inputNum=num
                shouldBreak=False

                while(num!=num[::-1]):
                    try:
                        num =str(int(num) + int(num[::-1]))
                    except:
                        print(f"\n{inputNum} is probably a Lychrel number")
                        shouldBreak=input()
                        break

                if(shouldBreak):
                    break
                startNum+=1
        case "2":
            while(True):
                iteration=0

                num = input("your num is:")
                inputNum=num
                shouldBreak=False

                if(num.isdigit()):
                    while(num!=num[::-1]):
                        iteration+=1
                        sys.stdout.write("\r{0} iteration".format(iteration))
                        sys.stdout.flush()
                        try:
                            num =str(int(num) + int(num[::-1]))
                        except:
                            print(f"\n{inputNum} is probably a Lychrel number")
                            shouldBreak=True
                            break
                    if(shouldBreak):
                        break
                    print(f"\n{num}")
                else:
                    break



