'''
Created on 2/13/2020
@author:   Timothy Stephens
Pledge:    I pledge that I have abided by the Stevens Honor System.
CS115 - Lab2
Implements recursion "Use It or Lose It" strategy.
'''
import sys
from cs115 import *

def change(amount, coins):
    """Evaluates a desired amount of money and a set of coins to determine the least
    amount of coins needed to equal the change."""
    if amount==0:
        return 0
    if coins==[]:
        return float("inf")
    if amount < coins[0]:
        return change(amount,coins[1:])
    else:
        lose= change(amount,coins[1:])
        use= 1 + change(amount-coins[0],coins)
        return min(use,lose)
    
    
