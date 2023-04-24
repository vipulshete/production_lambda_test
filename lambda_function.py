import boto3

def lambda_handler(event, context):
    # Get the source bucket and key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Specify the destination bucket and key
    destination_bucket = 'sensor-data-streaming'
    destination_key =  source_key
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Copy the object to the destination bucket
    s3_client.copy_object(
        Bucket=destination_bucket,
        Key=destination_key,
        CopySource={'Bucket': source_bucket, 'Key': source_key}
    )
    
    print(f'Successfully copied object from {source_bucket}/{source_key} to {destination_bucket}/{destination_key}')
