import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == "0":
        break
    else:
        r_num = num[::-1]
        if num == r_num:
            print("yes")
        else:
            print("no")
