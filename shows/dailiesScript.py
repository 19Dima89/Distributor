from utility import fileCollector
import os
import paramiko
from utility import dailiesInfo

def moveDailies(downloadDirectory, sftp, dbconnection):
    sftp.chdir("/HDD2/Dailies/")
    fileList = []
    
    cur = dbconnection.cursor()
    cur.execute("""SELECT * from dailies""")
    rows = cur.fetchall()
        
    for row in rows:
        fileList += fileCollector.getFiles(downloadDirectory, row[0], "*")
        
    for file in fileList:
        info = dailiesInfo.gatherInformation(file)
        
        if info == None:
            continue
        
        if info[0] in sftp.listdir():
            sftp.chdir(info[0])
        else:
            sftp.mkdir(sftp.getcwd()+info[0])
            sftp.chdir(info[0])
        
        if "Season "+info[1] in sftp.listdir():
            sftp.chdir("Season "+info[1])
        else:
            sftp.mkdir(sftp.getcwd()+"Season "+info[1])
            sftp.chdir("Season "+info[1])
            
        #copy the file to the current folder
        filepath = sftp.getcwd()+file
        localpath = downloadDirectory+file
        sftp.put(localpath, filepath)
        os.remove(downloadDirectory+file)
        
        sftp.chdir("../..")