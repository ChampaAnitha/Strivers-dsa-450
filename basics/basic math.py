# BASIC MATH - 24-10-23

# 1. You are given a number ’n’. Find the number of digits of ‘n’ that evenly divide ‘n’
def countDigits(n: int) -> int:   #parameterized function , n -> argument will return type int 
    count = 0
    temp = n  # Temporary variable to store the value of n . So orginla value of n is not lost 

#iteration through the n
    while temp > 0:  #ex:336 first 6>0 yes loop , 3 >0 loop , 3>0 loop nothing 0 >0 false count will be returned 
        digit = temp % 10  # Extract the last digit . ' % ' gives remainder 
        if digit != 0 and n % digit == 0:  # Check if digit is not 0 and if it divides n
            count += 1  #count is used for no of iteration 
        temp //= 10  # Remove the last digit from the number . '// ' floor function in division 

    return count   # count - no of times n is divisible - 336 is divisible 3 times so count=3.
print(countDigits(35))   # Expected: 1
print(countDigits(373))  # Expected: 0
print(countDigits(336))  # Expected: 3
print ("************************************************")

# 2. 

