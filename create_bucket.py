import boto3
import uuid

def create_bucket_name(bucket_prefix):
    #Bucket name must be between 3 and 63 characters
    return ''.join([bucket_prefix, str(uuid.uuid4())])
# print(create_bucket_name('test_first_bucket_'))

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.Session(profile_name='EC')
    current_region = session.region_name 
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name)
    print(bucket_name, current_region)
    return bucket_name, bucket_response


#Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
#[Clang 6.0 (clang-600.0.57)] on darwin
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import boto3
#>>> from create_bucket import create_bucket
#>>> session = boto3.Session(profile_name='EC')
#>>> 
#>>> s3_resource = session.resource('s3')
#>>> 
#>>> 
#>>> print(s3_resource)
#s3.ServiceResource()
#>>> s3_resource
#s3.ServiceResource()
#>>> type(s3_resource)
#<class 'boto3.resources.factory.s3.ServiceResource'>
#>>> first_bucket_name, first_reponse = create_bucket(
#... bucket_prefix='firstpythonbucket',
#... s3_connection=s3_resource.meta.client)
#firstpythonbucketb4e2e6b7-aebf-4c48-b8cd-86b0348906bb us-east-1





