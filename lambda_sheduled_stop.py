import boto3

client = boto3.client('ec2',region_name="ap-south-1")
def lambda_handler(event, context):
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Env',
                'Values': [
                    'Dev',
                ]
            },
        ]
    )
    a = response['Reservations']
    for x in a:
        b = x['Instances'][0]['InstanceId']
        c = x['Instances'][0]['State']['Name']
        # print(d)
        res = client.stop_instances(
            InstanceIds=[b]
        )
        print(res)
