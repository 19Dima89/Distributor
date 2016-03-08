import paramiko
import os
from utility import fileCollector
from utility import tvShowInfo

def moveTVShows(downloadDirectory, sftp):
    sftp.chdir("/HDD2/TV-Series/")

    fileList = fileCollector.getFiles(downloadDirectory, "*", "*")

    for file in fileList:
        info = tvShowInfo.gatherInformation(file)
        
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