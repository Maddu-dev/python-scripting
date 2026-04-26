import boto3

s3 = boto3.client('s3')

#Specify the file to upload
filename = 'boto3s3.txt'
bucket_name = 'job-auto-assets-maddu'
destfile = 'botonewfile.txt'

s3.upload_file(filename, bucket_name, destfile )
print("uploaded")