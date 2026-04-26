import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances( 
    ImageId = 'ami-098e39bafa7e7303d',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't3.micro',
    KeyName = 'docker-demo',
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Pythontest'
                },
                {
                    'Key': 'Department',
                    'Value': 'Technical',
                },
                {
                    'Key': 'Environment',
                    'Value': 'Test'
                }
            ]
        }
    ],
    BlockDeviceMappings = [
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,  # 20 GB root volume
                'VolumeType': 'gp2',  # General Purpose SSD
                'DeleteOnTermination': False
            }
        }
        
    ]    
)