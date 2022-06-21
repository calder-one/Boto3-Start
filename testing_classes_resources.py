import boto3

session = boto3.Session(profile_name='EC')

s3_resource = session.resource('s3')
s3_client = session.client('s3')

response = s3_resource.meta.client.list_buckets()

print(response)