#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:17:05 2022

@author: jumman
"""

# %%
"""
Write a function that gets an int number (n) as an input and prints all its factors
. The function returns the number of factors printed. For example, if n is 150, 
the function will print 
2 
3 
5 
5
"""
def factors(number):
    """return all the factor number of given number"""
    remain = number
    divisor  = 2
    #factorlist = []
    try:
        while remain != 0:
            if(remain % divisor == 0):
                #factorlist.append(divisor)
                print(divisor)
                remain = remain / divisor
                if remain == 0 or remain == 1:
                    break
                
            else:
                divisor += 1
                # if divisor == number:
                #     break
    except:
        print("There is an error")