# QA About Modules
1. What is the difference between ``import My_Module`` and ``from My_Module import *``?
    1. ``import My_module`` simply imports the module ``My_Module`` into the current program/name space. To access anything within ``My_Module`` I use the ``My_Module`` name with the "dot notation": (e.g. ``My_module.function1()``)
    1. ``from My_Module import *`` imports into the current program/name space all the functions, variables, classes, etc. defined in ``My_Module``. Since all these functions have been imported directly into your program, you do not access them via the ``My_Module``: e.g. you would invoke ``function1()`` directly.
    1. ``from My_module import *`` is generally frowned upon. First, you can get "name collisions" consider the following:
~~~~
In [1]: from math import *
In [2]: from cmath import *
In [3]: sqrt(9)
Out[3]: (3+0j)
In [4]: sqrt(-1)
Out[4]: 1j
~~~~
    1. Here the ``sqrt`` defined in ``cmath`` is hiding the ``sqrt`` defined in math. So while I may think I'm getting a function defined only for non-negative real numbers, I ended up with a function defined over the complex plane.
    e. From a learning perspective, I think the ``from My_Module import *`` is problematic because if I have multiple ``from X import *`` statements in my code, I don't know what module some function I'm using was defined in.

2. When do you know if you have to name the module before calling the function? (How would I Know that I have to use ‘math.’)? For example ``math.sqrt(121)`` vs ``sqrt(121)``
    1. These all relates to how it was imported the ``math.sqrt()`` corresponds to ``import math`` and ``sqrt(121)`` corresponds to ``from math import *`` (the function ``sqrt`` was imported directly into your program).
3. For: ``from random import *; print(random())``
What is this showing? What is ‘random()’?
    1. ``random()`` is a function defined in the module ``random``. You will see this a lot: a function with the same name as the module it is defined in.
4. Can you please explain what ``(modulename).__name__`` does?
    1. When Python imports a module it creates this attribute ``__name__``. Depending on how the module is being used ``__name__`` has a different value: if it is being imported, as we're talking about here it will have a value equal to the module name. If it is being used as a program, ``__name__`` will have the value ``__main__``. We'll go over this in class.

5. When I run print(``math.__file__``) I get the following error: module ``‘math’ has no attribute ‘__file__’``. What does this error message mean?
    1. While Python is generally cross-platform, it doesn't always operate identically across platforms. I think you are seeing a Windows specific issue. I only ever use ``__file__`` for debugging. To check that Python is using the file I think it is using. The ``__name__`` attribute is much more fundamental.
6. Can you explain what you are doing with this code (I do not get sys or sys.path):
~~~
import sys
import os
sys.path
~~~
    1. ``import sys``: import the ``sys`` module into my program.
    1. ``import os``: import the ``os`` module into my program
    1. ``sys.path``: access the ``path`` variable defined in ``sys``. It is a list of directory names.

7. I am still getting errors when I try to execute the import statements:
``import something_craziest``
``ImportError: No module named 'something_craziest'``
    1. The directory where ``something_craziest`` is located is not in ``sys.path``.

8. Where did the ``reverseMyName`` command come from in this statement?
print(chapmanbe.my_favorite_functions.reverseMyName("Brian","Chapman"))
    1. ``reverseMyName`` is a function defined in the module ``my_favorite_functions`` which is located in the package ``chapmanbe``.

9. This link is not working ``https://docs.python.org/lib/lib.htm.``
    1. Python changed their directory structure seems I made the notebook. Look at: [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)
