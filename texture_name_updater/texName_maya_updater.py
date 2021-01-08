#To be run inside of Maya
#TO DO: Basic UI

import pymel.core as pm
import json

json_path = 'path/texture_name_updater/texName_output/asset_modified.json'

file_nodes_lst = pm.ls(tex = True)

with open(json_path, 'r') as filehandle:
        updated_names_lst = json.load(filehandle)

reference_lst = [x[0] for x in updated_names_lst]

for i, texture_node in enumerate(file_nodes_lst):
    if pm.attributeQuery('fileTextureName', n=texture_node, ex=True) or pm.attributeQuery('filename', n=texture_node, ex=True):
        texture_node.setAttr('ignoreColorSpaceFileRules', True) # Ignoring temporarily to keep node colorspace

        if pm.attributeQuery('filename', n=texture_node, ex=True):
            attr_name = 'filename' # aiImage
        else:
            attr_name = 'fileTextureName' # Maya file

        absolute_path = texture_node.getAttr(attr_name).replace('\\', '/')
        original_name = absolute_path.split('/')[-1]
        absolute_dir = "/".join(absolute_path.split('/')[:-1]) + '/'
        
        if len(set(reference_lst).intersection(set([original_name]))) != 0:
            updated_name_index = reference_lst.index(original_name)
            updated_name = updated_names_lst[updated_name_index][2]
            
            new_path = absolute_dir + updated_name
            
            print('NODE: ' + texture_node + ' |||| FILENAME: ' + original_name + ' >>> ' + updated_name)
            
            texture_node.setAttr(attr_name, new_path)
        texture_node.setAttr('ignoreColorSpaceFileRules', False)
