import time
pi = 3.14
const1 = 4/3
const2 = pi * const1
print("*"*48,"\n","*gets the volume of a sphere given it's radius*\n","*"*48)
userinput = input("input radius of a sphere:")
try:
    userinput = int(userinput)
except:
    print("please enter a valid number")
    time.sleep(5)
    exit()
userinput = userinput ** 3
userinput = userinput * const2
print("(4/3)(3.14)(",userinput,")^3")
print("volume =",userinput,"units^3")
