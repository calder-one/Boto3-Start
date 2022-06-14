import boto3
import uuid

session = boto3.Session(profile_name='EC')
s3_client = session.client('s3')
s3_resource = session.resource('s3')

response = s3_client.list_buckets()

print("Existing Buckets: ")
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')

