# Idea 1: Simple program. 
    # Program structure: main function and other funcitons.  
    # Modules: Used. 
    # Paradigm: Procedural.
    # Unknown: Efficiency, (needs to learnt).
    # TO DO: Better output/customised message e.g. word/sentence into either word or sentence.
    # For Repeated words the permutations are: n!/a1! * a2!... ak!. 
    # Note for large inputs, the code doesn't scale well. 
        # Needs to be done in O(n log n) or such notions.
        
# Modules
from itertools import *


# Helper Functions
def factorial(n: int) -> int: 
    if n == 1 or n == 0: 
        return 1
    return n * factorial(n - 1)

def permutation(n: int,k: int) -> int:
    return factorial(n) // factorial(n - k)

def combination(n: int,k: int) -> int:
    return factorial(n) // (factorial(n - k) * factorial(k))

def tab_printed(*args): 
    print("\t",*args)


# Main program. 
def main(): 
    characters = list('boat')
    input_given = input('Enter a word/sequence of letters; default is "boat", press enter: ')
    input_given = input_given.lower()
    
    if ' ' in input_given: 
        input_given = ''.join(input_given.split())


    if input_given != '': 
       characters = input_given  
    len_characters = len(characters) 
    num_of_strings,i = 0, 1
    
    print("--", "This program prints all the possible string combinations of the following characters.", "--")
    
    while i <= len_characters: 
       num_of_strings += permutation(len_characters,i) 
       i += 1
    tab_printed(", ".join(characters))
    tab_printed("Number of strings that will be formed:", num_of_strings)
    
    #1. Choose a substring or the string itself & outting permutation of the string. 
    g_counter, i, n = repeat(1,3) 
    while i <= len_characters: 
        print("for", i, "letter word/split")

        for seq in permutations(characters,i): 
            print(n,''.join(seq))
            n += 1
        
        n = 1         
        i += 1

if __name__ == '__main__': 
    main()
