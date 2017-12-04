"""
Module demonstrating higher order functions, based on
"Learn you a Haskell"

"""


def zip_with(func, seq1, seq2):
    """
    zips seq1 and seq2 with func being applied to each paired element

    Arguments:
        func: A Python taking two Arguments
        seq1: A sequence
        sea2: A sequence

    Returns:
        A list
    """

    if not seq1 or not seq2:
        return []
    return [func(seq1[0], seq2[0])] +\
                zip_with(func, seq1[1:], seq2[1:])

def flip(func, arg1, arg2):
    """
    Takes a func and flips it

    Arguments:
        func: a python function that takes two argument
        arg1: first argument 
        arg2: second argument 
    """

    return func(arg2, arg1)

def map(f, seq):
    if not seq:
        return []
    return [f(seq[0])] + map(f,seq[1:])

def _filter(f, seq):
    if not seq:
        return []
    s = seq[0]
    seq2 = seq[1:]
    if f(s) :
        return [s] + _filter(f, seq2)
    return _filter(f,seq2)

def sort(seq):

    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    else:
        p  =  seq[0]
        return sort(filter(lambda x: x<= p, seq[1:])) + \
               [p] + \
               sort(filter(lambda x: x > p, seq[1:])) 
