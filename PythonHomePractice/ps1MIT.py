#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:30:22 2022

@author: jumman
"""

def numberOfMonths():
    """How many months it will take to save up enough money for a dwon payment"""
    
    #user interaction 
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    
    #simple calculation
    portion_down_payment = total_cost * 0.25
    current_savings = 0
    monthly_salary = annual_salary / 12
    number_of_months = 0
    
    #TODO main calculation
    
    return number_of_months