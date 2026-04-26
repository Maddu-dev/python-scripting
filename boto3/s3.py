import boto3

s3 = boto3.client('s3')
filename = 'botonewfile.txt'
bucket_name = 'job-auto-assets-maddu'
destfile = 'boto3s3.txt'

s3.download_file(bucket_name, filename, destfile)
