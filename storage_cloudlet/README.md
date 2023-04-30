# Storage Cloudlet Setup
1. Create an EC2 instance (Amazon Linux) with your security group and key pair.
2. Assign an IAM role with the "AmazonS3FullAccess" policy to the instance.
3. Connect the instance.
3. Run the following commands:
```
sudo yum update -y
sudo yum install git -y
sudo yum -y install python-pip
git clone https://github.com/austinmclain/RISE-Cloudlets.git
cd RISE-Cloudlets/storage_cloudlet
pip install virtualenv
virtualenv -p python3 my-env
source my-env/bin/activate
pip install -r requirements.txt
python3 main.py
```
