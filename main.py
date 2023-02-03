import sys

# sys.set_int_max_str_digits(1000000)

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



