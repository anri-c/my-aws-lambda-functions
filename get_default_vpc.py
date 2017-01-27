# coding: utf-8

import boto3

client = boto3.client('ec2')

## describe default VPC
vpc_filter = [
        {'Name':'isDefault', 'Values':['true']}
        ]

default_vpc = client.describe_vpcs(Filters=vpc_filter)
default_vpc_id = default_vpc['Vpcs'][0]['VpcId']

## describe default security group
security_group_filter = [
    {'Name': 'vpc-id', 'Values':[default_vpc_id]},
    {'Name':'group-name', 'Values':['default']}
    ]

default_security_group = client.describe_security_groups(Filters=security_group_filter)
default_security_group_id = default_security_group['SecurityGroups'][0]['GroupId']

def default_vpc_handler(event, context):
    return {
        'default_vpc_id': default_vpc_id,
        'default_security_group_id': default_security_group_id
        }
