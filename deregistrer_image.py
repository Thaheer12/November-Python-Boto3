import boto3
client = boto3.client('ec2',region_name="ap-south-1")
response = client.describe_instances()
a = response['Reservations']
d_amis=[]
for x in a:
    b = x["Instances"]
    for y in b:
        d_amis.append(y["ImageId"])
print(d_amis)
used_amis = []
for s in d_amis:
    if s not in used_amis:
        used_amis.append(s)
print(used_amis)

avalable_amis = client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
    ],
        Owners=[
            'self',
        ]
        )
d =  avalable_amis['Images']
coustom_amis=[]
for z in d:
    coustom_amis.append(z['ImageId'])
print(coustom_amis)
for amis in coustom_amis:
    if amis not in used_amis:
        p ="Deregisterting amis {}".format(amis)
        print(p)
        client.deregister_image(
            ImageId=amis)
