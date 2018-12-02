import boto3
client = boto3.client('ec2',region_name="ap-south-1")
#sns = boto3.client('sns',region_name="us-east-1")
response = client.describe_instances()
used_amis = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])
print(used_amis)

response = client.describe_images(
                    Filters=[
                            {
                                'Name': 'state',
                                'Values': [
                                    'available',
                                ]
                            },
                        ],
        Owners=[
        'self'
    ]
        )

# print(response)
custom_amis = []
for image in response['Images']:
    custom_amis.append((image['ImageId']))
print(custom_amis)

for ami in custom_amis:
    if used_amis not in used_amis:
        print(ami)
#         client.deregister_image(
#         ImageId=image['ImageId'])

