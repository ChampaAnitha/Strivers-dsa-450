# PASS BY VALUE & REFERENCE --> OBJECT REFERNCE    ''' 23-10-23 '''
''' c++ to python 
python doesn't have pass by value / reference instead as object reference '''

'''Functions - Take this coding challenge to test your coding skills to
-define a function
-pass arguments by value to a function
-pass arguments by reference to a function
This coding challenge is organized in the following way:

First line of input reads an integer to select the coding challenge:
-Reading value '1' selects the coding-challenge 1 ( tests the ability to define a function and pass arguments by value.-Reading value '2' selects the coding challenge 2 (tests the ability to pass arguments by reference to a function)
Coding Challenge -1
Define a function named "Maximum" that accepts two integers (pass by value) as arguments and returns the greatest of the two arguments.
Coding Challenge -2
Define a function named "Swap" that accepts two integers (pass by reference) as arguments and swaps their value.
Detailed explanation ( Input/output format, Notes, Images )
keyboard_arrow_down
Sample Input 1:
1
2 3
Sample Output 1:
3
Explanation Of Sample Input 1 :
The maximum of 2 and 3 is 3.
Sample Input 2:
2
4 5
Sample Output 2:
5 4
Explanation Of Sample Input 2 :
The values 4 and 5 are swapped.
Expected Time Complexity :
The expected time complexity is O(1).
Constraints :
1 <= 'test' <= 2
0 <= 'a', 'b' <= 10^9
Time limit: 1 second'''

def maximum(x, y):  # Pass by value (default in Python)
    return x if x > y else y

def swap(x, y):  # Python functions can't modify simple data types directly, so we'll return the swapped values
    x, y = y, x    # can only modify list & dict not tuple / string 
    return x, y

def main():
    test = int(input())
    a, b = map(int, input().split())
    
    if test == 1:
        r = maximum(a, b)
        print(r)
    elif test == 2:
        a, b = swap(a, b)
        print(a, b)
    else:
        print("Invalid test option")

if __name__ == "__main__":
    main()
