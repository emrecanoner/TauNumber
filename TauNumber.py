def check(num):
    counter = 0
    for x in range(1, num+1):
        if(num % x == 0):
            counter +=1
    if(num % counter == 0):
        print(num , "is a Tau Number")
    else:
        print(num , "is not a Tau Number")

check(8)
check(9)
check(12)
check(18)
check(20)
check(22)
check(24)
check(41)
