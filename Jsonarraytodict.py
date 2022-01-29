import os 
import json 

dict_components = {} # Getting the dictionary of the component in the json array data 
f = open("/mnt/c/Users/Kornbotdev/AppData/Local/Programs/Robotics_nodes_json/codeconfiggen.json") # Getting the code config gen json to running on the code system 
datacom = json.load(f)
Check_found_components = [] # Get the found components data inside the list
components = ['Imagesensor','MCU','Computeronboard','SensorArray','Navigationsensor','AmplifiermoduleIC'] # Getting the components  
print(datacom)
for ire in range(0,len(datacom)): 
        print(datacom[ire]) # Getting the ire 
        if len(datacom[ire]) == 2: 
                dict_components[datacom[ire][0]] = datacom[ire][1] 
        if len(datacom[ire]) >2: 
                 getsplit_com = datacom[ire].split(":")
                 top_dat = datacom[ire][0]
                 dict_components[getsplit_com[0]] = getsplit_com[1] 
print(dict_components) 
print(list(dict_components)) # Getting the list key for the topic classification 
for ir in list(dict_components): 
         print("Components",ir) # Getting the string header function to running inside the conditioning status control 
         if ir.split(",")[0] in components: 
                    print("Found the components",ir.split(",")[0])
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Write the output file into the usable function output 
json_dumpcom = json.dumps(dict_components)
writejson_Com = open("Components_node_robotics.json","w")
writejson_Com.write(json_dumpcom) #Write the json component 
writejson_Com.close()            
    

