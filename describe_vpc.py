import boto3
client=boto3.client("ec2",region_name="us-east-1")
response = client.describe_vpcs()
a = response["Vpcs"]
count = 0
for x in a:
    b = x['CidrBlock']
    c = x['VpcId']
    d = x['InstanceTenancy']
    print("VPC ID is {} and VPC CIDR is {} and its tendency is {}".format(c,b,d))
    count = count+1
print("Total vpc are {}".format(count))
