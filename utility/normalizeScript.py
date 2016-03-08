from utility import fileCollector
import os
import re

def normalizeFileNames(downloadDirectory, dbconnection):
    
    cur = dbconnection.cursor()
    cur.execute("""SELECT * from normalize""")
    rows = cur.fetchall()
    
    fileList = fileCollector.getFiles(downloadDirectory, "*", "*")
    
    for file in fileList:
        
        nameOfCurrentFile = file
        
        for row in rows:
            regex = re.compile(row[0])
            nameOfCurrentFile = re.sub(regex, row[1], nameOfCurrentFile)
        
        obj = re.search(r'\.\d{4}\.', nameOfCurrentFile)
            
        if obj == None:
            obj = re.search(r'\.\d{3}\.', nameOfCurrentFile)
            
        if obj == None:
            os.rename(file, nameOfCurrentFile)
            continue
                
        substitute = obj.group()[1:len(obj.group())-1] 
                
        if len(obj.group()) == 6:
            nameOfCurrentFile = re.sub(substitute, "S"+substitute[:2]+"E"+substitute[2:], nameOfCurrentFile)
        else:
            nameOfCurrentFile = re.sub(substitute, "S0"+substitute[0]+"E"+substitute[1:], nameOfCurrentFile)
        
        os.rename(file, nameOfCurrentFile)