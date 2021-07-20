# Simple Dynamic DNS script (writes to AWS Route53)

This is a simple python script that finds the network's public IP and updates a DNS record in AWS Route53.

You can run this as a python script, or create and run a Docker image.
This script was written using Python 3.9.

## Getting started

To get this script running you need to prepare a couple of things described in the section below.

### AWS Credentials

to document

### AWS Route53 Hosted Zone

to document

You need to tell the script which DNS zone to update. You do this by [finding the Hosted Zone ID in the AWS Console](https://console.aws.amazon.com/route53/v2/hostedzones) and providing it as environment variable to the script.

For example: `HOSTED_ZONE_ID=ABC123`

### The DNS record to set

You can tell the script which DNS name to update using the `DYNAMIC_DNS_NAME` environment variable. For example:


```
DYNAMIC_DNS_NAME=subdomain.example.org
```


## Running the script (plain python)

Running the Python script requires two steps. Assuming you are in the `./src` directory:

1. Install python dependencies: `pip install -r requirements.txt`
2. Run the script: `HOSTED_ZONE_ID=ABC123 DYNAMIC_DNS_NAME=subdomain.example.org python main.py`

## Run using Docker

Running the script using docker requires two steps. Assuming you are in the project root directory:

1. Build the docker image: `docker build -t aws-dynamicdns:latest .`
2. To run the docker image once: `docker run --rm -ti -e HOSTED_ZONE_ID=ABC123 -e DYNAMIC_DNS_NAME=subdomain.example.org aws-dynamicdns:latest`

## License

See LICENSE.md in this repository