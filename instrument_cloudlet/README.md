# SEM Setup
1. Create an EC2 instance (Amazon Linux) with your security group and key pair.

The EC2 instance is now ready to be used as a mock SEM.

# Instrument Cloudlet Setup
### Note: Before continuing, please navigate to the storage cloudlet directory and follow the instructions there.
For now, the instrument cloudlet must be set up locally.
1. Run the following commands on your local machine:
```
git clone https://github.com/austinmclain/RISE-Cloudlets.git
cd RISE-Cloudlets/instrument_cloudlet
virtualenv -p python3 my-env
source my-env/bin/activate
pip install -r requirements.txt
```
2. Add this information to [config.py](https://github.com/austinmclain/RISE-Cloudlets/blob/main/instrument_cloudlet/config.py):
- Hostname of SEM EC2 instance (public IPv4 address)
- Username of SEM EC2 instance (default username is `ec2-user`)
- Absolute path to your downloaded SEM EC2 key pair
- URL of storage cloudlet in this format `<ipv4 of storage cloudlet>:8081/storageApi/`
3. Start the API with the following command:
```
python3 main.py
```
If you are having trouble with any dependencies, it may be helpful to look at the commands given in the storage cloudlet directory.

4. Send a POST request [here](https://www.postman.com/amac72/workspace/rise-cloudlets/collection/24318566-e5b1f778-aec0-4718-aad2-08f2412231ab?action=share&creator=24318566) using Postman.
