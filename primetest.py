currentnumber = 2#                          [won't be accurate if you try starting from a higher number.]
prime1 = 2                            
prime2 = 0                      
prime3 = 0
prime4 = 0
prime5 = 0
prime6 = 0
prime7 = 0
prime8 = 0          #                       [you'll have to manually add more variables              ]
prime9 = 0          #                       [to increase the accurate range.                         ]
legacyvariable1 = 0#                       [variables up to prime n gives correct results up to n^2.]                     

while currentnumber < 841:                 #[remember to increase to prime n^2 if your expanding the range.]
   
    mod = currentnumber % prime1 
    if mod == 0 and currentnumber != prime1:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
   
    elif prime2 !=0 and currentnumber % prime2 == 0 and currentnumber != prime2:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
    
    elif prime3 !=0 and currentnumber % prime3 == 0 and currentnumber != prime3:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
   
    elif prime4 !=0 and currentnumber % prime4 == 0 and currentnumber != prime4:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
   
    elif prime5 !=0 and currentnumber % prime5 == 0 and currentnumber != prime5:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
   
    elif prime6 !=0 and currentnumber % prime6 == 0 and currentnumber != prime6:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
  
    elif prime7 !=0 and currentnumber % prime7 == 0 and currentnumber != prime7:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
   
    elif prime8 !=0 and currentnumber % prime8 == 0 and currentnumber != prime8:
        print(currentnumber)
        print("is not prime")
        currentnumber = currentnumber + 1
    
    elif prime9 !=0 and currentnumber % prime9 == 0 and currentnumber != prime9:# [you'll have to add more of these         ]
        print(currentnumber)                                                    # [to increase the range. remember to change]
        print("is not prime")                                                   # [ALL the relevant variables on each one.  ]
        currentnumber = currentnumber + 1
    
    else:
        print(currentnumber)
        print("is prime")
        #if legacyvariable1 == 0:                                                 [you'll have do to uncomment this]
        #    prime1 = currentnumber                                               [and do other stuff to start     ]
        #    legacyvariable1 = 1                                                  [from 1 and avoid hardcoding in 2.]
        if prime2 == 0 and currentnumber != 2:
            prime2 = currentnumber
        elif prime3 == 0:
            prime3 = currentnumber
        elif prime4 == 0:
            prime4 = currentnumber
        elif prime5 == 0:
            prime5 = currentnumber
        elif prime6 == 0:
            prime6 = currentnumber
        elif prime7 == 0:
            prime7= currentnumber
        elif prime8 == 0:
            prime8 = currentnumber
        elif prime9 == 0:                #                                       [you'll have to add more of these         ] 
            prime9 = currentnumber       #                                       [to increase the range. remember to change]        
        currentnumber = currentnumber + 1#                                       [ALL the relevant variables on each one.  ]
