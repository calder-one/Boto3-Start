import boto3
import uuid

def create_bucket_name(bucket_prefix):
    #Bucket name must be between 3 and 63 characters
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name 
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

# print(create_bucket_name('test_first_bucket_'))