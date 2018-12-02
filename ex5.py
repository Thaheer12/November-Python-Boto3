a={
  'version': '0',
  'id': '1a50ae2f-01a2-c879-4ee4-9146bba9c895',
  'detail-type': 'EC2 Instance State-change Notification',
  'source': 'aws.ec2',
  'account': '115935572748',
  'time': '2018-12-02T06:26:10Z',
  'region': 'ap-south-1',
  'resources': [
    'arn:aws:ec2:ap-south-1:115935572748:instance/i-0c00004ca8f6be57b'
  ],
  'detail': {
    'instance-id': 'i-0c00004ca8f6be57b',
    'state': 'stopped'
  }
}
b = a['region']
c= a['detail']['instance-id']
d = a['detail']['state']
print("In region '{}' with instance id '{}' and its state is '{}'".format(b,c,d))

