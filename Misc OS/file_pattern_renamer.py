#!/usr/env/python

import os 
import sys

path = sys.argv[1]
target_pattern =  sys.argv[2]
new_pattern = sys.argv[3]

path = path + '\\' if path[-1] is not '\\' else path

file_lst = file_lst = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for f in file_lst:
    print(f,'>>>',f.replace(target_pattern, new_pattern))
    os.rename(path + f, path + f.replace(target_pattern, new_pattern))
