from utility import fileCollector
import os
import paramiko

def moveDailies(downloadDirectory, sftp, dbconnection):
    dailyDirectory = "/HDD2/Dailies/"
    
    cur = dbconnection.cursor()
    cur.execute("""SELECT * from dailies""")
    rows = cur.fetchall()
        
    for row in rows:
        list = fileCollector.getFiles(downloadDirectory, row[0], "*")
        
        for l in list:
            filepath = dailyDirectory+row[1]+l
            localpath = downloadDirectory+l
            sftp.put(localpath, filepath)
            os.remove(downloadDirectory+l)