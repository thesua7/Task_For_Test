import json
import os
from itertools import chain

MainData={}
annotation_objects = {}
vehicle = {}
license_plate = {}
vehicleAttr={}
licenseAttr={}
annotation_attributes = {}

def buildingStockStructure(nameofDataset):

    
    MainData['dataset_name'] = nameofDataset
    MainData['image_link'] = None
    MainData['annotation_type'] = "image"
    vehicle['presence']=0
    vehicle['bbox'] = []
    annotation_objects['vehicle']=vehicle
    MainData['annotation_objects'] = annotation_objects
    vehicleAttr['Type']=None
    vehicleAttr['Pose']=None
    vehicleAttr['Model']=None
    vehicleAttr['Make']=None
    vehicleAttr['Color']=None
    annotation_attributes['vehicle']=vehicleAttr
    MainData['annotation_attributes'] = annotation_attributes
    license_plate['presence']=0
    license_plate['bbox'] = []
    annotation_objects['license_plate']=license_plate
    MainData['annotation_objects'] = annotation_objects
    licenseAttr['Difficulty Score'] = None
    licenseAttr['Value'] = None
    licenseAttr['Occlusion'] =None
    annotation_attributes['license_plate']=licenseAttr
    MainData['annotation_attributes'] = annotation_attributes

def generateJsonFromFile(nameofDataset,pathTemp):

        fp = open(pathTemp, 'r+');

        data = json.load(fp)
        jtopy=json.dumps(data) 
        dict_json=json.loads(jtopy) 





        if len(dict_json['objects'])==0:
            buildingStockStructure(nameofDataset)
        else:
            for i in data['objects']:
             check =i['classTitle'] 
             if check.__eq__("Vehicle"):
                MainData['dataset_name'] = nameofDataset
                MainData['image_link'] = None
                MainData['annotation_type'] = "image"
                vehicle['presence']=1
                flatten_list = list(chain.from_iterable(i['points']['exterior']))
                vehicle['bbox'] = flatten_list
                annotation_objects['vehicle']=vehicle

                MainData['annotation_objects'] = annotation_objects
                
                for each in i['tags']:
                    vehicleAttr[each['name']]=each['value']

                annotation_attributes['vehicle']=vehicleAttr
                MainData['annotation_attributes'] = annotation_attributes


            if  check.__eq__("License Plate"):
                        MainData['dataset_name'] = nameofDataset
                        MainData['image_link'] = ""
                        MainData['annotation_type'] = "image"
                        license_plate['presence']=1
                        flatten_list = list(chain.from_iterable(i['points']['exterior']))
                        license_plate['bbox'] = flatten_list
                        annotation_objects['license_plate']=license_plate
                        MainData['annotation_objects'] = annotation_objects
                        for each in i['tags']:
                            licenseAttr[each['name']]=each['value']
                        
                        licenseAttr['Occlusion'] =0
                        annotation_attributes['license_plate']=licenseAttr
                        MainData['annotation_attributes'] = annotation_attributes

        print(MainData)
        fileSavePlace = "\json_files"
    
        with open("json_files/test_formatted_"+nameofDataset, "w") as outfile:
            json.dump(MainData, outfile)






file0 = "\json_files\pos_0.png.json"
path0 = os.getcwd()+file0

datasetName0 = os.path.basename(path0)
generateJsonFromFile(datasetName0,path0)

file10010 = "\json_files\pos_10010.png.json"
path10010 = os.getcwd()+file10010
datasetName10010 = os.path.basename(path10010)
generateJsonFromFile(datasetName10010,path10010)

file10492 = "\json_files\pos_10492.png.json"
path10492 = os.getcwd()+file10492
datasetName10492 = os.path.basename(path10492)
generateJsonFromFile(datasetName10492,path10492)