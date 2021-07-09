import json, os, pickle
from typing import final

def read_json(path):
    with open(path) as f:
        converted_to_json_obj = json.load(f)
        #loading converts a str to json object. Remember dbm are stored as str while json is readable
    return converted_to_json_obj

#print(read_json('/Users/sean/labs/PyPart9/data/super_smash_bros/link.json'))


def read_all_json_files(path):
    json_list = []
    for root, dir, files in os.walk(path):
        files = [f for f in files if not f[0] == '.' and f.endswith('.json')]
        #print('files printed: ' + str(files) + '\n')
        for i in files:
            #print('i: ' + str(type(i)) + '\n')
            #print(type(root))
            #print('dir: ' + str(dir))
            #print('path joined: ' + os.path.join(root, i))
            json_list.append(read_json(os.path.join(root, i)))
    return json_list
        
#print(read_all_json_files('/Users/sean/labs/PyPart9/data/super_smash_bros'))


def write_pickle(path):
    with open('/Users/sean/labs/PyPart9/**super_smash_characters.pickle**', 'wb') as f:
        pickle.dump(read_all_json_files(path), f)
        #dumping converts the value to a str from an object
        #pickling converts obj to str that can be stored in a database
        #struggled with figuring out why my load_pickle wasn't returning anything. Noticed my SSB pickle file had a reference to the path instead of the
        #contents of the path. Realized I'm dumping the path instead of the values in the path. Need to call read_all_json_files to add contents

def load_pickle(path_to_load): 
    finalOutput = ''
    with open(path_to_load, 'rb') as f:
        output = pickle.load(f)
        for line in output:
            print(str(line) + '\n')
            finalOutput += str(line)
    return finalOutput
        



#write_pickle('/Users/sean/labs/PyPart9/data/super_smash_bros copy')
load_pickle('/Users/sean/labs/PyPart9/**super_smash_characters.pickle**')
#print(read_json('/Users/sean/labs/PyPart9/data/super_smash_bros/link copy 3.json'))

if __name__ == 'main':
    read_json
    read_all_json_files
    write_pickle
    load_pickle