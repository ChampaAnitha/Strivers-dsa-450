''' HASHING - 12-11-23 
Python provides built-in support for hashing through the hash() function. The hash() function is used to generate a hash value (an integer) for a given object. This hash value is commonly used in hash tables and dictionaries for quick data retrieval.'''

# 1. count the frequency 
from typing import *

def countFrequency(n: int, x: int, nums: List[int]) -> int:
    ans = [0 for _ in range(n)]

    for i in range(len(nums)):        #n=6
        if nums[i] <= n:            #num=[1,2,3,4,7,2]  , # i = 1 , i=2 , i=3
            ans[nums[i]-1] += 1         #num[0]=1 , num[1]=2
    return ans  

# 2. highest & lowest frequency 
from collections import Counter
from typing import List

def getFrequencies(v: List[int]) -> List[int]:
    # Create a Counter object to count the frequencies of elements.
    freq = Counter(v)

    # Initializing variables to determine.
    # Maximum frequency and minimum frequency element.
    maxFreq = 0
    minFreq = float('inf')
    maxElement = 0
    minElement = float('inf')
    
    # Traverse through Counter to find the elements.
    for element, count in freq.items():
        if count > maxFreq:
            # Found an element with frequency maximum among 
            # all elements found till now.
            maxElement = element
            maxFreq = count
        elif count == maxFreq:
            # Checking if the current element is smaller or not.     
            maxElement = min(maxElement, element)
        
        if count < minFreq:
            # Found an element with frequency minimum among 
            # all elements found till now.
            minElement = element
            minFreq = count
        elif count == minFreq:
            # Checking if the current element is smaller or not.         
            minElement = min(minElement, element)
    
    ans = [maxElement, minElement]
    return ans
