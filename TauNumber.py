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