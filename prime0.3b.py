currentnumber = 1
prime = []
ticklimit = -1
check = 0
check2 = 1
while currentnumber < 160:
    if currentnumber == 7 or currentnumber == 2:
        print("test")
    tick = 0
    while tick <= ticklimit and check == 0 and ticklimit != -1:
        check2 = 0
        if currentnumber % prime[tick] == 0 and prime[tick] != 1 and currentnumber != 1:
            #currentnumber = currentnumber + 1
            check = 2
        elif tick < ticklimit:
            tick = tick + 1
            check = 0
        else:
            check = 1
            tick = 0
    
    if currentnumber != 1 and check2 == 1 or check == 1:
        print(currentnumber)
        print("is prime")
        print(ticklimit)
        check = 0
        prime.append(currentnumber)
        currentnumber = currentnumber + 1
        ticklimit = ticklimit + 1
        print(prime)
        print(ticklimit)
    elif currentnumber == 1:
        print("1 yo")
        check = 0
        currentnumber = currentnumber + 1
    else:
        currentnumber = currentnumber + 1