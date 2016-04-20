def nextC(m):
    if (m % 2 == 0):
        m //= 2
    else:
        m = (3 * m) +1
    return(m)

def superCollatz(n):
    M = 2
    step = 0
    unique = []
    check = []
    steps = []
    while M < n:
        if M in check:
            print("Progress: Skipped ", M)
            M += 1
        else:
            m = M                 #make a new variable to work with with the value of the unique number
            unique.append(m)      #add newest unique value to out
            check.append(m)       #add value to check
            while m != 1:
                m=nextC(m)        #do collatz
                step += 1         #add 1 to step for every step until you get to 1
                check.append(m)     #add every value you encounter to check
            if m == 1:              #when you get to 1
                steps.append(step)  #add to stepscount
                step = 0
                print("Progress: Computed Collatz ", M)
    if M == n:
        if M in check:
            print("Progress: Skipped ", M)
            out=list(zip(unique,steps))
            return(out)
        else:
            m = M
            unique.append(m)
            check.append(m)
            while m != 1:
                m=nextC(m)
                step += 1
                check.append(m)
            if m == 1:
                steps.append(step)
                out=list(zip(unique,steps))
                print("Progress: Computed Collatz ",M)
        return(out)
     
#n=int(input("Enter an integer: "))
#k=superCollatz(n)
#print(k)
