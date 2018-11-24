import boto3
vpc=boto3.client("ec2",region_name="us-east-1")
res = vpc.create_vpc(
    CidrBlock='145.123.0.0/16'
)

# res={'Vpc': {'CidrBlock': '145.123.0.0/16', 'DhcpOptionsId': 'dopt-6cc53914', 'State': 'pending', 'VpcId': 'vpc-0f420b8c917c9c1ca', 'InstanceTenancy': 'default', 'Ipv6CidrBlockAssociationSet': [], 'CidrBlockAssociationSet': [{'AssociationId': 'vpc-cidr-assoc-0d901b4244fc9e897', 'CidrBlock': '145.123.0.0/16', 'CidrBlockState': {'State': 'associated'}}], 'IsDefault': False, 'Tags': []}, 'ResponseMetadata': {'RequestId': '1f0f2eef-7288-4498-a2db-33fde2ecb737', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'text/xml;charset=UTF-8', 'content-length': '929', 'date': 'Sat, 24 Nov 2018 05:11:40 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
a= res["Vpc"]['CidrBlock']
b= res["Vpc"]['VpcId']
c=res["Vpc"]['InstanceTenancy']
print("VPC ID is {} and its CIDR block is {} and its tendency is {}".format(b,a,c))
