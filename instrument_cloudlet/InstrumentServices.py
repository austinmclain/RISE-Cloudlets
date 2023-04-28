from paramiko import SSHClient, AutoAddPolicy
import requests
import base64

class InstrumentServices:
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
        
    def runCommand(self, cmd):
        try:
            (stdin, stdout, stderr) = self.client.exec_command(cmd)
            cmd_output = stdout.read().decode()
            self.client.close()
            return{"status": 1, "msg": "command ran successfully", "data": cmd_output}
        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}
        
    def __downloadImage(self, remotePath, localPath):
        try:
            sftp = self.client.open_sftp()
            sftp.get(remotePath, localPath)
            sftp.close()
            self.client.close()
            return{"status": 1, "msg": "image downloaded successfully", "data": localPath}
        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}

    def uploadImage(self, remotePath, localPath):
        try:
            self.__downloadImage(remotePath, localPath)
            with open(localPath, 'rb') as f:
                contents = base64.b64encode(f.read())
                # Configuration specific to storage cloudlet
                r = requests.post('http://52.91.224.85:8081/storageApi/receiveImage', contents)
                return{"status": r.status_code}
        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}
