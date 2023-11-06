def checkPrime(n):
    if n <= 1 :
        return False
    elif n <= 3 :
        return True
    elif n%2==0 or n%3==0 :
        return False
    

n = int(input("Enter a number: "))
result = checkPrime(n)



