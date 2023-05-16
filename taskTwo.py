import json
import os
import pandas as pd
from collections import defaultdict


file1= "\json_files\pos_0.png.json"
path1 = os.getcwd()+file1
fp1 = open(path1, 'r+');
data1 = json.load(fp1)


file2= "\json_files\pos_10010.png.json"
path2 = os.getcwd()+file2
fp2 = open(path2, 'r+');
data2 = json.load(fp2)

file3= "\json_files\pos_10492.png.json"
path3 = os.getcwd()+file3
fp3 = open(path3, 'r+');
data3 = json.load(fp3)


def merge_dict(d1,d2, d3):        #took help from
    dd = defaultdict(list)        #https://stackoverflow.com/questions/66059820/merge-two-json-object-in-python  
    countV = 0
    for d in (d1,d2, d3):

        for key, value in d.items():
            countV= countV+1
          
            if isinstance(value, list):
                dd[key].extend(value)
            else:
                dd[key].append(value)

    return dict(dd)


json_str1 = json.dumps(data1)
json_str2 = json.dumps(data2)
json_str3 = json.dumps(data3)

dct1 = json.loads(json_str1)
dct2 = json.loads(json_str2)
dct3 = json.loads(json_str3)

combined_dct = merge_dict(dct1,dct2, dct3)




for i in combined_dct['objects']:
    if i['classTitle'].__eq__("Vehicle"):
        i['classTitle'] = "car"
    
    if  i['classTitle'].__eq__("License Plate"):
        i['classTitle'] = "number"



print(combined_dct)

fileSavePlace = "\json_files"

with open("json_files/single_json.json","w") as outfile:
    json.dump(combined_dct, outfile)

