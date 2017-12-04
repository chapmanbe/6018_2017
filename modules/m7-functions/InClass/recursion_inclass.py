# ## Solving the problem using recursion
# 
# Recursive functions are functions that call themselves. This is usually done instead of a implementing a loop.

# ### [factorial](https://en.wikipedia.org/wiki/Factorial): A famous recursive function
# 
# The factorial function (usually depicted as $n!$), is the product of all positive integers less than $n$. $0!$ is defined to be 1 ($0! := 1$).
# 
# * The domain of the factorial function is?
# * The range of the factorial function is?
# 


def factorial(n):
    """
    computes the factorial of the integer n

    Arguments:
        n: a non-negative integer

    Returns:
        An integer
    """
    if n < 0:
        raise ValueError("%s: n must be a non-negative integer"%n)
    if type(n) != int:
        raise ValueError("%s: n must be an intger"%n)
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


def fibonacci(n):
    """
    Computes the nth Fibonacci number

    Arguments:
        n: a non-negative intger

    Returns:
        An integer
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def get_pos_integer_take2(prompt="Enter a positive integer"):
    """
    returns a positive integers. The function is called recursively
    until a positive integer is provided by the user.

    Arguments:
        prompt: A string to prompt the user

    returns:
        An integer

    """
    try:
        num = int(input(prompt))
        if num <0:
            return get_pos_integer_take2(prompt)
        else:
            return num
    except ValueError:
        return get_pos_integer_take2(prompt=prompt)


def maximum(vals):
    """
    Recursively computes the maximum value in a collection

    Arguments:
        vals: a list of ordinal values

    returns:
        The numberic maximum in vals
    """
    if len(vals) == 0:
        raise ValueError(" No maximum in an empty list")
    if len(vals) == 1:
        return vals[0]
    else:
        return max(vals[0], maximum(vals[1:]))


def replicate(num, val):
    """
    Returns a list ov num instances of ValueError

    Arguments:
        num: a non-negative integers
        val: va value to replicate

    Returns:
        a list
    """
    if num == 0:
        return []
    elif num == 1:
        return [val]
    else:
        return [val] + replicate(num-1,val)


def take(num, seq):
    """
    Take the first num elements from seq 

    Arguments:

        num: a non-negative number
        seq: a sequence of values

    Returns:
        A list
    """
    if num <= 0:
        return []
    elif len(seq) == 0:
        return []
    else:
        return [seq[0]] + take(num-1, seq[1:])


def reverse(seq):
    """
    Returns a reverse version of seq 

    Arguments:
        seq: a sequence

    Returns:
        A reversed version of seq
    """
    if len(seq) == 0:
        return []
    else:
        return [seq[-1]] + reverse(seq[:-1])

def zip(seq1, seq2):
    """
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return []
    else:
        return [(seq1[0], seq2[0])] + zip(seq1[1:], seq2[1:])


def elem(val, seq):
    """
    Checks if val is in seq

    Arguments:

        val: Some Python ValueError
        seq: A Python sequence
    Returns:
        boolean

    """
    if len(seq) == 0:
        return False
    elif val == seq[0]:
        return True
    else:
        return elem(val, seq[1:])


def sort(seq):
    if len(seq) == 0:
        return []
    elif len(seq) == 1:
        return seq
    else:
        p  =  seq[0]
        return sort([pp for pp in seq if pp <= p]) + \
               [p] + \
               sort([pp for pp in seq if pp > p]) 
