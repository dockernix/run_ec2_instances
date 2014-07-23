#!/usr/bin/python2
import boto


user_data = open('bootstrap.sh')

conn = boto.connect_ec2('XXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


reservation = conn.run_instances(image_id='ami-018c9568',
                                 instance_type='t1.micro',
                                 security_groups=['devops'],
                                 key_name='devops',
                                 user_data=user_data.read()
                                 )
print reservation
