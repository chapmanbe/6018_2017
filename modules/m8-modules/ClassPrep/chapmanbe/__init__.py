"""This is the __init__ file for the chapmanbe package"""

__all__ = ["my_favorite_functions"]
from . import my_favorite_functions
import getpass
import os
creator_name = "Brian Chapman"
your_name = getpass.getuser()

package_data_dir = os.path.join(os.path.expanduser('~'),".%s"%your_name)
if not os.path.exists(package_data_dir):
    os.mkdir(package_data_dir)
