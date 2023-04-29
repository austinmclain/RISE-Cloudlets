from paramiko import SSHClient, AutoAddPolicy
import requests
import base64
import random

from config import instrument_1, storage_cloudlet

class InstrumentServices:
    def __init__(self):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.load_system_host_keys()

        self.client.connect(hostname=instrument_1['hostname'], 
                            username=instrument_1['username'],
                            key_filename=instrument_1['key_filename'])
        
    def __uploadToSem(self, sftp, id):
        sftp.put(f'./images/img${id}.png', f'img${id}.png')

    def __downloadFromSem(self, sftp, id):
        sftp.get(f'img${id}.png', f'img${id}.png')

    def __uploadToStorageCloudlet(self, image):
        with open(image, 'rb') as f:
            contents = base64.b64encode(f.read())
            r = requests.post(storage_cloudlet['url'], contents)
            return r.status_code
        
    def runExperiment(self):
        try:
            sftp = self.client.open_sftp()
            id = random.randint(1, 4)
            self.__uploadToSem(sftp, id)
            sftp.close()
            self.client.close()
            return {"status": 1, "msg": "command ran successfully", "data": f'img${id}.png'}
        except Exception as e:
            return {"status": 0, "msg": "error msg " + str(e)}
    
    def saveImage(self, id):
        try:
            sftp = self.client.open_sftp()
            self.__downloadFromSem(sftp, id)
            sftp.close()
            self.client.close()
            status = self.__uploadToStorageCloudlet(f'img${id}.png')
            return {"status": 1, "msg": "image saved successfully", "status": status}
        except Exception as e:
            return {"status": 0, "msg": "error msg " + str(e)}
