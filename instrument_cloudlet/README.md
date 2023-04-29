# SEM Setup
1. Create an EC2 instance (Amazon Linux) with default settings.

The EC2 instance is now ready to be used as a mock SEM.

# Instrument Cloudlet Setup
1. Create an EC2 instance (Amazon Linux) with default settings.
2. SSH into the instance.
3. Run the following commands:
```
sudo yum update -y
sudo yum install git -y
sudo yum -y install python-pip
git clone https://github.com/austinmclain/RISE-Cloudlets.git
cd RISE-Cloudlets/instrument_cloudlet
pip install virtualenv
virtualenv -p python3 my-env
source my-env/bin/activate
pip install -r requirements.txt
python3 main.py
```