# Storage Cloudlet Setup
1. Create an S3 bucket.
2. Create an EC2 instance (Amazon Linux) with your security group and key pair.
3. Assign an IAM role with the "AmazonS3FullAccess" policy to the EC2 instance.
4. Connect to the instance.
5. Run the following commands:
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
```
6. Confirm that the S3 information found in StorageServices.py is correct.
7. Start the API with the following command:
```
python3 main.py
```
