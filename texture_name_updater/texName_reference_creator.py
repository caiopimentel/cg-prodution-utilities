#!/usr/env/python
import hashlib
import os
import sys
import json

original_list = []
directory = sys.argv[1]
main_dir = '_'.join(directory.split('\\')[-3:-1])
behavior = sys.argv[2]
fileList = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
output_dir = 'texName_output'

for f in fileList:
    with open(directory + f, 'rb') as texture_file:
        hasher = hashlib.md5()
        buf = texture_file.read()
        hasher.update(buf)

    original_list.append([f,hasher.hexdigest()])

if not os.path.exists('./' + output_dir):
    os.makedirs('./' + output_dir)

if behavior == 'c':
    with open('./' + output_dir + '/%s_original.json' % main_dir, 'w') as filehandle:
        json.dump(original_list, filehandle)

elif behavior == 'u':
    with open('./' + output_dir + '/%s_original.json' % main_dir, 'r') as filehandle:
        updated_list = json.load(filehandle)

    for i, value in enumerate(original_list):
        hash_location = [x[1] for x in updated_list].index(original_list[i][1])
        updated_list[hash_location].append(original_list[i][0])
        
    with open('./' + output_dir + '/%s_modified.json' % main_dir, 'w') as filehandle:
        json.dump(updated_list, filehandle)

    print(updated_list)