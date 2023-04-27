from paramiko import SSHClient, AutoAddPolicy
import requests

def ssh_connection(cmd):
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

    try:
        (stdin, stdout, stderr) = client.exec_command(cmd)
        cmd_output = stdout.read().decode()
        print('Output:\n', cmd_output)
        client.close()
        # save = input('Would you like to save this image? (y/n): ')
        # if (save == 'y'):
        #     r = requests.get('http://localhost:8080')
        #     print(r.content)
        return{"status": 1, "msg": "command ran successfully", "data": cmd_output}

    except Exception as e:
        print(str(e))
        return{"status": 0, "msg": "Error msg " + str(e)}
