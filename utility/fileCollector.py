import glob, os

def getFiles(directory, showName, extension):
    """This function fills the list variable witch alle the files in 'directory'"""
    os.chdir(directory)
    
    list = []
    
    for file in glob.glob("*"+showName+"*."+extension):
        list.append(file)
        
    return list
