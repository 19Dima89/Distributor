import paramiko
import sys

class FastTransport(paramiko.Transport):
    def __init__(self, sock):
        super(FastTransport, self).__init__(sock)
        self.window_size = 2147483647
        self.packetizer.REKEY_BYTES = pow(2, 40)
        self.packetizer.REKEY_PACKETS = pow(2, 40)
        
def getSFTPConnection(host, port, user, passwd):
    try:
        ssh_conn = FastTransport((host, port))
        ssh_conn.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(ssh_conn)
        returnList = {"sftp":sftp, "ssh_conn":ssh_conn}
        #returnList.append(sftp)
        #returnList.append(ssh_conn)
        return returnList
    except:
        print "No connection to the host could be established"
        sys.exit(0)