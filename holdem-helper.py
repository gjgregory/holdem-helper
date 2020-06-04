#!/usr/bin/env python3
"""
Module documentation.
"""

# Imports
import sys

# Global variables

# Class declarations

# Function declarations

def getCardString(value, suit):
    parts = ['+-----+\n|', value, '    |\n|     |\n|  ', suit,
            '  |\n|     |\n|    ', value, '|\n+-----+']
    return ''.join(['%s' %p for p in parts])

def printCards():
    print(getCardString('K', '♡'))

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [-options] [inputs] ')
        sys.exit(1)

    printCards()

# Main body
if __name__ == '__main__':
    main()
