# t2_imports.py

# Step 1: import package 1- __init__.py run hota hai 2- core.py load hoti hai  3-aur ye line run hoti hai: 4-print("core imported") 5-utils.py load hoti hai print no
import pkg_demo

# call function return 42 output
print(pkg_demo.answer())


# Step 2: import * python check and import __all__ waly bs
from pkg_demo import *

print(safe_div(10, 2))
print(safe_div(10, 0))