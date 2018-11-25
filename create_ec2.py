import boto3

client = boto3.client('ec2', region_name="us-east-1")
response = client.run_instances(
                ImageId='ami-09479453c5cde9639',
                InstanceType='t2.micro',
                SubnetId='subnet-0ac2acd59318805c7',
                MaxCount=1,
                MinCount=1,
                SecurityGroupIds=['sg-04e04c737d3473d89'])
print(response)