import infofile
from samples import samples
import numpy as np

tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/" # web address

def get_fileString_list():
    fileString_list = []
    for s in samples: # loop over samples
        for val in samples[s]['list']: # loop over each file
            if s == 'data': prefix = "Data/" # Data prefix
            else: # MC prefix
                prefix = "MC/mc_"+str(infofile.infos[val]["DSID"])+"."
            fileString = tuple_path+prefix+val+".4lep.root" # file name to open
            fileString_list.append(fileString)
    return fileString_list
    
def get_val_list():    
    val_list = []
        for val in samples[s]['list']: # loop over each file
            val_list.append(val)
    return val_list

def get_file_array(fileString_list, val_list):
    file array = np.array([fileString_list, val_list]).T
