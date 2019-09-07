#_author:无言宝宝
#date:  2019/8/5

import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import The_main_interface

The_main_interface.Feature_selection()