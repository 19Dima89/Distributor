from utility import tvShowInfo
from utility import fileCollector
from utility import normalizeScript
from utility import paramikoConnection
from shows import dailiesScript
from shows import tvShowScript
from shows import realityScript
import psycopg2
import paramiko
import sys
import os

downloadDirectory = "/home/doom/Downloads/sambaDir/"

#If .part files are present in the downloadDirectory exit the script
partFiles = fileCollector.getFiles(downloadDirectory, "*", "part")

if len(partFiles) != 0:
    sys.exit(0)

#Open database connection
try:
    dbconnection = psycopg2.connect("dbname='DistributorDB' user='xxx' host='xxx' password='xxx' connect_timeout=5")
except:
    print "No connection to the database could be established!"
    sys.exit(0)

#SFTP Authentication
host = "xxx"
port = 000

password = "xxx"
username = "xxx"

#Establish SFTP connection    
connection = paramikoConnection.getSFTPConnection(host, port, username, password)
sftp = connection["sftp"]
ssh = connection["ssh_conn"]
    
#Copy all dailies to their designated directory
dailiesScript.moveDailies(downloadDirectory, sftp, dbconnection)

#Normalize all remaining file names, so they can be further processed
normalizeScript.normalizeFileNames(downloadDirectory, dbconnection)

#Copy all the reality shows to their designated directory
realityScript.moveRealityShows(downloadDirectory, sftp, dbconnection)

#Copy all the 'normal' shows to their designated directory
tvShowScript.moveTVShows(downloadDirectory, sftp)

#Close sftp connection
sftp.close()
ssh.close()