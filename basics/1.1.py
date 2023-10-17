''' USES NESTED LOOP 
1. CHECK INNER & OUTER LOOP 
2. FOR OL [ ] - count the no of lines
3. FOR IL- focus on column connect with rows '''

#4 * 4 pattern 
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#5 * 1 pattern 
for i in range(1, 6):  # Outer loop runs 5 times (i = 1 to 5 inclusive)
    for j in range(i):  # Inner loop runs 'i' times
        print('*', end=' ')
    print()  # Move to the next line after printing stars for each row

# 5 *1  ( no edition )
for i in range(1, 6):     # Outer loop runs 5 times (i = 1 to 5 inclusive)
    for j in range(1, i+1):   # Inner loop runs 'i' times
        print(j, end=' ')  # Print the current value of j followed by a space
    print()              # Move to the next line after printing numbers for each row

for i in range(1, 6):  # Outer loop runs 5 times (i = 1 to 5 inclusive)
    for j in range(3,5):  # Inner loop runs 'i' times
        
        print('*', end=' ')
    print()  
        