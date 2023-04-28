from paramiko import SSHClient, AutoAddPolicy
import requests
import os

def ssh_connection(cmd, goal='other'):
    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.load_system_host_keys()

        # Configuration specific to EC2 instance acting as SEM
        client.connect('3.80.102.76', username='ec2-user',
                    key_filename= "/Users/amac/Desktop/rise-project-key.pem")

    except Exception as e:
        print(str(e))
        return{"status": 0, "msg": "Connection not established with server"}
    
    # If goal is to download...
    if (goal == 'download'):
        try:
            sftp = client.open_sftp()
            localpath = 'image_1'
            remotepath = 'experiment_1/Misc_pollen.jpg'
            sftp.get(remotepath, localpath)
            sftp.close()
            client.close()
            return{"status": 1, "msg": "command ran successfully", "data": localpath}
        except Exception as e:
            print(str(e))
            return{"status": 0, "msg": "Error msg " + str(e)}

    try:
        (stdin, stdout, stderr) = client.exec_command(cmd)
        cmd_output = stdout.read().decode()
        print('Output:\n', cmd_output)
        client.close()
        return{"status": 1, "msg": "command ran successfully", "data": cmd_output}

    except Exception as e:
        print(str(e))
        return{"status": 0, "msg": "Error msg " + str(e)}
