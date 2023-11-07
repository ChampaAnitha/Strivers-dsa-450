''' RECURSION - 1  [7-11-23] '''

# 1. You are given an integer ‘n’. Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.
from typing import List

def printNos(x: int) -> List[int]:
    def generate_numbers(i, n):
        if i > n:   #base condition
            return [] #empty list 
        else:
            return [i] + generate_numbers(i + 1, n)  #recursion
             #list - appending all values 
    return generate_numbers(1, x)  #after recursion gives final output x=temporary storage of n 

def main():
    n = int(input())
    result = printNos(n)
    print(result)

if __name__ == "__main__":
    main()

# 2. You are given an integer ‘n’. Return an array having “Coding Ninjas” ‘n’ times, without using a loop.

from typing import List

def printNtimes(n: int) -> None:
    if n > 0: #base condition 
        print("Coding Ninjas", end=" ")
        printNtimes(n - 1)  #recursion

def main():
    n = int(input())
    printNtimes(n)

if __name__ == "__main__":
    main()

# 3. n to 1 recursively 
from typing import List

def generate_numbers(i, n, result):
    if i < 1:   #base condition
        return result
    result.append(i)  #print (i)
    return generate_numbers(i - 1, n, result) #recursion f(i-1,n)

def printNos(x: int) -> List[int]:
    result = []
    return generate_numbers(x, x, result) #f(n,n)

def main():
    n = int(input())
    result = printNos(n)
    for num in result:
        print(num, end=" ")

if __name__ == "__main__":
    main()

# 4. 1 to n recursively 
from typing import List

def generate_numbers(i, n, result):
    if i > n:  #base condition
        return result
    result.append(i)
    return generate_numbers(i + 1, n, result)  #f(1,n)

def printNos(x: int) -> List[int]:
    result = []
    return generate_numbers(1, x, result)  #f(1,n)

def main():
    n = int(input())
    result = printNos(n)
    for num in result:
        print(num, end=" ")

if __name__ == "__main__":
    main()

# 5. sum of n natural no
def sumFirstN(n: int) -> int:
    return n * (n + 1) // 2    # n(n+1)/2

def main():
    n = int(input("Enter a positive integer: "))
    result = sumFirstN(n)
    print("The sum of the first", n, "natural numbers is:", result)

if __name__ == "__main__":
    main()

# 6.  sum of n natural no parameter

# 7 . sum of n natural no functional

# 8 . reverse an array 

# 9 . check palindrome

# 10 . fibonacci noo       
def fib(n):
    if n<=1:
        return n 
    return fib(n-1)+fib(n-2)

def main():
    n=int(input()) 
    print(fib(n))

if __name__ == "__main__":
    main()                                                              