import boto3
import botocore
import os
import urllib3
import sys

if 'HOSTED_ZONE_ID' in os.environ is not None:
    pass
else:
    print('Please provide the HOSTED_ZONE_ID environment variable')
    sys.exit(1)

if 'DYNAMIC_DNS_NAME' in os.environ is not None:
    pass
else:
    print('Please provide the DYNAMIC_DNS_NAME environment variable')
    sys.exit(1)

awsHostedZoneId = os.environ['HOSTED_ZONE_ID']
dynamicDnsName = os.environ['DYNAMIC_DNS_NAME']


client = urllib3.PoolManager()
response = client.request('GET', 'https://ifconfig.co', headers={'Accept': 'text/plain'})
myIp = response.data.decode('utf-8').strip()


try:
    route53 = boto3.client('route53')

    route53.change_resource_record_sets(
        HostedZoneId=awsHostedZoneId,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': dynamicDnsName,
                        'Type': 'A',
                        'TTL': 60,
                        'ResourceRecords': [
                            {
                                'Value': myIp
                            }
                        ]
                    }
                }
            ]
        }
    )

    print('Successfully updated DNS for ' + dynamicDnsName + ' to ' + myIp)

except botocore.exceptions.NoCredentialsError as error:
    print('Error: {error}'.format(error=error))