from nose.tools import assert_equal, assert_true
import numbers
import random

def literal_variables1(arg1=None, arg2=None):
    """
    arg1: 
    arg2:
    """
    try:
        assert_true(isinstance(arg1, str))
        print("arg1 is a string")
        try:
            assert_equal(arg1,"327")
            print("arg1 contains the correct value")
        except:
            print("While arg1 is correctly a string, the string does not contain the correct value")
    except:
        print("arg1 does not contains the correct data type")
    try:
        assert_true(isinstance(arg2,numbers.Number))
        print("arg2 is correctly a number")
        try:
            assert_true(isinstance(arg2,int))
            print("arg2 is correctly an integer")
        except:
            print("arg2 is not the correct type of number")
    except:
        print("arg2 was not set to a number type")


def test_quadratic(myfunc):
    x = random.randint(-10,10)
    x0 = random.randint(-10,10)
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    result =  myfunc(x,x0,a,b)
    if result == None:
        return "Your function is not correct. Did you forget to set a value for y or explicitly return a value?"
    if isinstance(result, numbers.Number):
        if result == (x-x0)**2 + a*x + b:
            return "Your function seems to be correct"
        else:
            return "Your function is returning a number but it is not the correct value."
    else:
        return "Your function is not returning a number as it is expected to."

def test_bmi(myfunc):
    mass = random.gauss(80, 15)
    height = random.gauss(165, 30)

    result =  myfunc(mass, height)
    if result == None:
        return "Your function is not correct. Did you forget to set a value for y or explicitly return a value?"
    if isinstance(result, numbers.Number):
        if result == mass/height**2:
            return "Your function seems to be correct"
        else:
            return "Your function is returning a number but it is not the correct value."
    else:
        return "Your function is not returning a number as it is expected to."

def test_random_integer(myfunc):
    results = []
    result =  myfunc()
    if result == None:
        return "Your function is not correct. Did you forget to set a value for y or explicitly return a value?"
    try:
        assert_true(isinstance(result, numbers.Number))
    except:
        return "Your function is not returning a number as it is expected to."
    try:
        assert_true(isinstance(result, int))
    except:
        return "Your function return a number but it was not an integer"
    for i in range(1000):
        result = myfunc()
        results.append(result)
        try:
            assert_true(20 <= result <= 50)
        except:
            return "Your function returned an integer but the value %d is not in the specified range"%result
    try:
        assert_true(20 in results and 50 in results)
    except:
        return "Your function is behaving properly but I'm suspicious that your range is not correct."
    return "Your function seems to be correct"
   
def test_nibabel():
    try:
        import nibabel
        return "It looks like nibabel is installed properly"
    except ImportError:
        return "It looks like nibabel is not installed"

def test_ply():
    try:
        import ply
        return "It looks like ply is installed properly"
    except ImportError:
        return "It looks like ply is not installed."

def test_pediatric_age(myfunc):

    def _ref(myage):
        if myage < 1:
            return "NEONATES"
        elif myage < 24:
            return "INFANTS"
        elif myage < 144:
            return "CHILDREN"
        elif myage < 12*16:
            return "ADOLESCENTS"
        else:
            return "OTHER"
    for i in range(100):
        age = random.randint(0,18*12)
        my_group = myfunc(age)
        ref_group = _ref(age)
        if my_group == None:
            return "Your function is not correct. Did you forget to set a value for y or explicitly return a value?"
    
        try:
            assert_equal(my_group, ref_group)
        except:
            return "You mapped the age %d to the group %s when the correct group was %s"%(age, my_group,  ref_group)
    return "Your function seems to be correct"
