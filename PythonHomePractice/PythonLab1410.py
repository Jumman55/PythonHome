#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:13:16 2022

@author: jumman
"""

# %%
    # calculating the epsilion or error calculating
from math import sqrt
    
def epsilion():
    r = sqrt(2)   
    if (abs(r*r - 2.0) <  0.00000001):
        print("sqrt(2.0) squered is 2.0")
    else:
        print("sqrt(2.0) squered is not 2.0")


# %%

def primeNumbervalidation(givenNumber):
    """Return the prime number treu or false"""
        
    k = 2
         
    if givenNumber%2 != 0:
            while k < givenNumber:
                 if givenNumber%k == 0:
                     return False
                 k += 1
            return True
    elif(givenNumber ==  2 ):
            return True
        
    elif(givenNumber == 1):
        return False
        
    else:
        print("Not prime")
        return False
        
# %% prof solution

def is_prime(x):
    """Return true if this is a prime number or false"""
    k = 2
    
    while x % k != 0 and k < x:
        k += 1
    if k == x:
        return True
    else:
        return False
    
# %%

def average_from_input():
    counter = 0
    total = 0
    while True:
        x = int(input("Give an int: "))
        
        if x == 0:
            break
        else:
            total += x
            counter += 1
    return (total / counter)