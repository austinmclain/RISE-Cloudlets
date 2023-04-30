# SEM Setup
1. Create an EC2 instance (Amazon Linux) with your security group and key pair.

The EC2 instance is now ready to be used as a mock SEM.

# Instrument Cloudlet Setup
### Note: Before continuing, please navigate to the storage cloudlet directory and follow the instructions there.
For now, the instrument cloudlet must be set up locally.
1. Run the following commands:
```
git clone https://github.com/austinmclain/RISE-Cloudlets.git
cd RISE-Cloudlets/instrument_cloudlet
virtualenv -p python3 my-env
source my-env/bin/activate
pip install -r requirements.txt
```
2. Add this information to config.py:
- Hostname of SEM (public IPv4 address)
- Username of SEM
- Full path to your downloaded SEM key pair
- URL of storage cloudlet
3. Start the API with the following command:
```
python3 main.py
```
If you are having trouble with any dependencies, it may be helpful to look at the commands given in the storage cloudlet directory.
