# BASIC MATH - 24-10-23 

# 1. You are given a number ’n’. Find the number of digits of ‘n’ that evenly divide ‘n’
def countDigits(n: int) -> int:   #parameterized function , n -> argument will return type int 
    count = 0
    temp = n  # Temporary variable to store the value of n . So orginla value of n is not lost 

#iteration through the n
    while temp > 0:  #ex:336 first 6>0 yes loop , 3 >0 loop , 3>0 loop nothing 0 >0 false count will be returned 
        lastdigit = temp % 10  # Extract the last digit . ' % ' gives remainder 
        if lastdigit != 0 and n % lastdigit == 0:  # Check if digit is not 0 and if it divides n
            count += 1  #count is used for no of iteration 
        temp //= 10  # Remove the last digit from the number . '// ' floor function in division 

    return count   # count - no of times n is divisible - 336 is divisible 3 times so count=3.
print(countDigits(35))   # Expected: 1
print(countDigits(373))  # Expected: 0
print(countDigits(336))  # Expected: 3
print ("************************************************")

# 2. palindrome (string&no)
def is_palindrome(n:int): 
    digit = int(str(n)[::-1]) #add int to make it string 
    return n == digit

# Usage example:
n = int(input())
if is_palindrome(n):
    print("true")
else:
    print("false")
print ("************************************************")

''' 4-11-23 , 5-11-23, 6-11-23'''
    
# 3. GCD - EUCLIDIAN METHOD 
def calcGDC(n: int, m: int) -> int:
    while m: #while m != 0:
        n, m = m, n % m
    return n
print(calcGDC(4,16))
print ("************************************************")

#4. Armstrong no
def armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        lastdigit = n % 10
        sum = sum + (lastdigit * lastdigit * lastdigit)
        n = n // 10
    return sum

n = int(input("Enter a number:"))
is_armstrong = armstrong(n)

if is_armstrong == n:
    print("True")
else:
    print("False")
print ("************************************************")

# 5. reverse a string / no
def reverse_number(n):
    reversed_num = 0
    temp=n
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num

n = int(input("Enter a number: "))
reversed_n = reverse_number(n)
print("Reversed number:", reversed_n)
print ("************************************************")

# 6. prime /not 
def checkPrime(n):
    if n <= 1 :
        return False
    elif n <= 3 :
        return True
    elif n%2==0 or n%3==0 :
        return False
print ("************************************************")

# 7. Extracting the digits - count , print digits 
def count_digits(n:int):
    count=0
    while n>0:
        n//=10
        count+=1
    return count

n=int(input("enter a no"))
print(count_digits(n))