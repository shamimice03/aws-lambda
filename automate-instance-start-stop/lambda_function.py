import json
import boto3

def lambda_handler(event, context):
    region = 'ap-northeast-1'
    client = boto3.client('ec2', region_name=region)
    
    tag_key = "Project"
    tag_value = "webapp"
    
    response = client.describe_instances(
        Filters=[
            { 'Name': f'tag:{tag_key}', 'Values': [tag_value] },
        ]
    )
    
    for instance in response['Reservations']:
        instanceId = instance['Instances'][0]['InstanceId']
        state = instance['Instances'][0]['State']['Name']
    
        if state == 'stopped':
            client.start_instances(InstanceIds=[instanceId])
        elif state == 'running':
            client.stop_instances(InstanceIds=[instanceId])
            
            
