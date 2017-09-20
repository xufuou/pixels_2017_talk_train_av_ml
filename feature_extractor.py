import os
import pefile
import pandas as pd

class PEFile:
    """
    This Class is constructed by parsing the pe file for the interesting features
    each pe file is an object by itself and we extract the needed information
    into a dictionary
    """
    def __init__(self, filename):
        self.pe = pefile.PE(filename, fast_load=True)
        self.filename = filename
        self.DebugSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
        self.DebugRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress
        self.ImageVersion = self.pe.OPTIONAL_HEADER.MajorImageVersion
        self.OSVersion = self.pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
        self.ExportRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
        self.ExportSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
        self.IATRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress
        self.ResSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size
        self.LinkerVersion = self.pe.OPTIONAL_HEADER.MajorLinkerVersion
        self.NumberOfSections = self.pe.FILE_HEADER.NumberOfSections
        self.StackReserveSize = self.pe.OPTIONAL_HEADER.SizeOfStackReserve
        self.Dll = self.pe.OPTIONAL_HEADER.DllCharacteristics

    def Construct(self):
        sample = {}
        for attr, k in self.__dict__.iteritems():
            if(attr != "pe"):
                sample[attr] = k
        return sample

def pe2vec(direct="dasmalwerk/archive/zippedMalware"):
    """
    dirty function (handling all exceptions) for each sample
    it construct a dictionary of dictionaries in the format:
    sample x : pe informations
    """
    dataset = {}
    for subdir, dirs, files in os.walk(direct):
        print files
    '''
            file_path = os.path.join(subdir, f)
            try:
                pe = pedump.PEFile(file_path)
                dataset[str(f)] = pe.Construct()
            except Exception as e:
                print e
    return dataset
    '''
def vec2csv(dataset):
    # now that we have a dictionary let's put it in a clean csv file
    df = pd.DataFrame(dataset)
    infected = df.transpose() # transpose to have the features as columns and samples as rows
    infected.to_csv('dataset.csv',sep=',', encoding='utf-8')
        
if __name__=='__main__':
    path = "dasmalwerk/binaries/e769b6ab-ef05-11e6-86ab-80e65024849a.file"
    pe = PEFile(path)
    sample = pe.Construct()
    
    print sample
