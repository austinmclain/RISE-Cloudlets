# RISE-Cloudlets
Cloudlet setup and APIs for RISE project. We simulate collecting images from a scanning electron microscope (SEM) with an instrument cloudlet. Then we simulate uploading the images to a storage cloudlet.

## Requirements
To set this system up, you will need:
- An AWS account
- A security group that allows all traffic
- A key pair

## Instructions
Start with the storage cloudlet instructions, then move on to the instrument cloudlet instructions.

- [Storage Cloudlet Instructions](https://github.com/austinmclain/RISE-Cloudlets/blob/main/storage_cloudlet/README.md)
- [Instrument Cloudlet Instructions](https://github.com/austinmclain/RISE-Cloudlets/blob/main/instrument_cloudlet/README.md)

By the end, you will have:
- Two EC2 instances, one to simulate the SEM and one for the storage cloudlet
- One S3 bucket

This will take about 10 minutes.

## Usage
You can test the system using the Postman requests found [here](https://www.postman.com/amac72/workspace/rise-cloudlets/collection/24318566-e5b1f778-aec0-4718-aad2-08f2412231ab?action=share&creator=24318566).

Send a POST request using Postman. You may need to create a Postman account. In order to send the POST requests to the local instrument API, please install Postman Desktop, then run the POST request from there.
