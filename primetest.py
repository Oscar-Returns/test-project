currentnumber = 1
currentprime = 0
prime = [1,1,1,1,1,1,1,1,1,1,1]
ticklimit = 0
check = 0
check2 = 0
while currentnumber < 100:
    tick = 0
    while tick <= ticklimit and check == 0:
        if currentnumber % prime[tick] == 0 and prime[tick] != 1 and currentnumber != 1:
            currentnumber = currentnumber + 1
            check = 0
            check2 = 2
        elif tick < ticklimit and check2 == 2:
            tick = tick + 1
        else:
            check = 1
            tick = 0

    if currentnumber != 1 and check == 1:
        print(currentnumber)
        print("is prime")
        check = 0
        prime[currentprime] = currentnumber
        currentnumber = currentnumber + 1
        currentprime = currentprime + 1
        ticklimit = ticklimit + 1
        print(prime)
    else:
        print("1 yo")
        check = 0
        currentnumber = currentnumber + 1