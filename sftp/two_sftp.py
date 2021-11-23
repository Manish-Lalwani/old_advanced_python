#reference from prathamesh code


import pysftp


sftpHost = "127.0.0.1"
sftpUserName = "xyz"
sftpPassword = "Dora456."
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None



def sftpConnection():
    try:
        print("Connecting to SFTP.")
        with pysftp.Connection(sftpHost, username=sftpUserName, password=sftpPassword, cnopts=cnopts) as sftp:
            #with sftp.cd(sftpFolderLoc):
             #   sftp.put(sftpSourceFilePath)
              #  sftpList = sftp.listdir()
            print("connection to host successful")
    except Exception as err:
        print("SFTP connection error ", err)




if __name__ == "__main__":

    sftpConnection()