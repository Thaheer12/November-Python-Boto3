import boto3

client = boto3.client('ec2',region_name="us-east-1")
# response = client.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='10.10.3.0/26',
#     VpcId='vpc-018e59b9cdc77b4f3'
# )
# print(response)

response = client.describe_subnets()
count=0
a=response['Subnets']
for x in a:
    b = x['SubnetId']
    c = x['VpcId']
    d = x['AvailabilityZone']
    e = x['Tags'][0]['Value']
    count=count+1
    # print(e)
    print("SUBNET ID '{}' with name '{}' which is present in Vpc-id '{}' and its availability zone is '{}'".format(b,e,c,d))
print("Total subnets are {}".format(count))