# emails
import re
firstnames = input("enter first name:")
secondnames = input("enter second name:")
years = input("enter year started:")
if re.search("^[a-zA-Z]+$", firstnames):
    initial = firstnames[0]
else:
    print("please enter a valid name")
try:
    yeardigits = years[2]
    yeardigits2 = years[3]
except:
    print("please enter a valid year")
email = initial + "." + secondnames + yeardigits + yeardigits2 + "@kishogecc.ie"
print(email)
