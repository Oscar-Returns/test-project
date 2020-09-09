currentnumber = 1            # won't work if you increase
prime = []                   # all primes stored here
ticklimit = -1               # how many primes are currently stored (don't ask why its negative)
check2 = 1                   # this can almost definitely be removed
while currentnumber < 100:   # change this to change limit of checked numbers
    check = 0                # don't know why i'm definig this again but whatever(doesn't work if you remove it)
    tick = 0                 # what prime number in the list is being checked
    while tick <= ticklimit != -1 and check == 0:#the actual checking prime factors loop
        check2 = 0
        if currentnumber % prime[tick] == 0 and prime[tick] != 1 and currentnumber != 1:
            check = 2
        elif tick < ticklimit:
            tick = tick + 1
            check = 0
        else:
            check = 1
            tick = 0

    if currentnumber != 1 and check2 == 1 or check == 1:#if the number's prime
        print(currentnumber, end = " ")
        print("is prime")
        check = 0
        prime.append(currentnumber)
        currentnumber = currentnumber + 1
        ticklimit = ticklimit + 1
    elif currentnumber == 1:                            #if it's one (1)
        print("1 isn't prime for some reason")
        check = 0
        currentnumber = currentnumber + 1
    else:                                               # if it's some other integer
        currentnumber = currentnumber + 1