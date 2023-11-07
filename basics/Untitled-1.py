def fib(n):
    if n<=1:
        return n 
    return fib(n-1)+fib(n-2)

def main():
    n=int(input("enter a no")) 
    print(fib(n))

if __name__ == "__main__":
    main()  