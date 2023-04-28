from paramiko import SSHClient, AutoAddPolicy
import requests
import os

class ssh_connection:
    def __init__(self):
        try:
            self.client = SSHClient()
            self.client.set_missing_host_key_policy(AutoAddPolicy())
            self.client.load_system_host_keys()

            # Configuration specific to EC2 instance acting as SEM
            self.client.connect('54.224.49.107', username='ec2-user',
                        key_filename= "/Users/amac/Desktop/rise-project-key.pem")

        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Connection not established with server"}
        
    def download(self, imagePath):
        try:
            sftp = self.client.open_sftp()
            localpath = 'image_1.jpg'
            remotepath = imagePath
            sftp.get(remotepath, localpath)
            sftp.close()
            self.client.close()
            return{"status": 1, "msg": "command ran successfully", "data": localpath}
        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}

    def command(self, cmd):
        try:
            (stdin, stdout, stderr) = self.client.exec_command(cmd)
            cmd_output = stdout.read().decode()
            self.client.close()
            return{"status": 1, "msg": "command ran successfully", "data": cmd_output}

        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}
