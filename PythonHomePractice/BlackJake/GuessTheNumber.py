#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:01:24 2022

@author: jumman
"""

# import random

# mainRandomNumber = random.randint(1, 100)

# def number_checker(inputNumber, randomNumber):
#     """to check the giver number higher lower or equal"""
#     if inputNumber == randomNumber:
#         return 0
    
#     elif inputNumber > randomNumber:
#         return 1
#     else:
#         return 2
    
# def play_game():
#     """Use as a main function"""
#     print("Wlcome to the number Guessing Game! \n I'm thinking of a number between 1 and 100.")

def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)

def fact(number, cn):
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)
    
