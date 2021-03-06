#!/usr/bin/env python3

"""
Slicing Lab

TASKS
Write some functions that take a sequence as an argument, and return a copy of that sequence:
    
    -with the first and last items exchanged.
    -with every other item removed.
    -with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    -with the elements reversed (just with slicing).
    
    -with the last third, then first third, then the middle third in the new order.
Author: Clifford Butler
"""

#sequences as an argument utilized for this module. 
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
    """ 
    Takes a sequence as an argument and returns a copy of the sequence,
    with the first and last items exchanged
    """
    first_part = seq[:1]
    last_part = seq[-1:]
    return last_part + seq[1:-1] + first_part

def every_other(seq):
    """
    Takes a sequence as an argument and returns a copy of the sequence,
    with every other item removed.
    """
    return seq[::2]

def remove_last4_first4_every_other(seq):
    """
    Takes a sequence as an argument and returns a copy of the sequence,
    with the first 4 and the last 4 items removed, 
    and then every other item in the remaining sequence.
    """
    return seq[4:-4:2]

def reverse_element(seq):
    """
    Takes a sequence as an argument and returns a copy of the sequence,
    with the elements reversed.
    """
    return seq[::-1]

def resequence(seq):
    """
    Takes a sequence as an argument and returns a copy of the sequence,
    with the last third, then first third, 
    then the middle third in the new order.
    """
    first = seq[:3]
    middle = seq[3:-3]
    last = seq[-3:]
    return last + first + middle

if __name__ == "__main__":
    # run some tests for exchange_fist_last(seq)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    
    # run some tests for every_other(seq)
    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)
    
    # run some tests for remove_last4_first4_every_other(seq)
    assert remove_last4_first4_every_other(a_string) == " sas"
    assert remove_last4_first4_every_other(a_tuple) == ()
    
    # run some tests for reverse_element(seq)
    assert reverse_element(a_string) == "gnirts a si siht"
    assert reverse_element(a_tuple) == (32, 5, 12, 13, 54, 2)
    
    # run some tests for reqequence(seq)
    assert resequence(a_string) == "ingthis is a str"
    assert resequence(a_tuple) == (12, 5, 32, 2, 54, 13)
    
    print("tests passed")
