from __future__ import print_function

import os
import sys

from run import calc


def main():
   """Bootstrap the app"""
   total = 0
   for i in range(100):
      total += calc(i)
      
   print(total)
      
      

if __name__ == '__main__':
   main()
   
   