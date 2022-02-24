import paramiko
import os
paramiko.util.log_to_file("paramiko.log")

# Open a transport
host,port = os.environ.get("host"),22
transport = paramiko.Transport((host,port))

# Auth    
username,password = os.environ.get("username"),os.environ.get("password")
transport.connect(None,username,password)

# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

remote_path = "/home/hpant/"
archive_path = "/home/hpant/archive"
for f in sftp.listdir_attr(remote_path):
    print(f)
    if (f.filename.endswith('csv')):
        remote_file_path = remote_path + "/" + f.filename
        archive_file_path = archive_path + "/" + f.filename
        print("Archiving %s to %s" % (remote_file_path, archive_file_path))
        print(remote_file_path)
        print(archive_file_path)
        sftp.rename(remote_file_path, archive_file_path)
