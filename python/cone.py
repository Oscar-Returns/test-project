import time
print("*"*48,"\n","*gets the volume of a cone given it's radius*\n","*"*48)
pi = 3.14
const1 = input("height of cone:")
try:
    const1 = int(const1)
except:
    print("please enter a valid number")
    time.sleep(5)
    exit()
const2 = pi * (const1/3)
userinput = input("input radius of cone:")
try:
    userinput = int(userinput)
except:
    print("please enter a valid number")
    time.sleep(5)
    exit()
userinput = userinput ** 2
userinput = userinput * const2
print("volume =",userinput,"units^3")
