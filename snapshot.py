import boto3
client = boto3.client('ec2',region_name="ap-south-1")
response = client.describe_volumes(
Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Dev',
            ]
        },
    ],
)
a = response['Volumes']
for x in a:
    y = x["Attachments"]
    t = y[0]["VolumeId"]
    print("Creating Snap shots are {}".format(t))
    client.create_snapshot(VolumeId=t)

# response = client.create_snapshot(
#
#     VolumeId='vol-05c56fc29a5e7f0c1')
# print(response)