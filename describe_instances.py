import boto3
client = boto3.client('ec2',region_name="us-east-1")
sns = boto3.client('sns',region_name="us-east-1")
z
    f = res['StoppingInstances'][0]['CurrentState']['Name']
    e = res['StoppingInstances'][0]['PreviousState']['Name']
    g = res['StoppingInstances'][0]['InstanceId']
    h = "instance id is {}, its previos state is {} andits current satate is {}".format(g,e,f)
    print(h)
    res1 = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:115935572748:Production_alerts',
        Message=h,
        Subject='PRO-ALERTS'
    )
