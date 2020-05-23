import boto3
import configparser
import sys
import time
config = configparser.ConfigParser()
config.sections()
config.read('ec2_devinstance.conf')
region=config['ec2']['region']
instance=config['ec2']['insance_id']
ec2 = boto3.client('ec2',region_name=config['ec2']['region'])

def stop_instances(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[
        instance_id,
    ],)
    except Exception as e:
        print(e)
    print("instance stopped successfully")
def start_instances(instance_id):
    try:
        ec2.start_instances(InstanceIds=[
        instance_id,
    ],)
    except Exception as e:
        print(e)
    print("instance started successfully")


def wait_for_action_completion(instance):
    required_state=""
    if action == 'stop':
        required_state = 'stopped'
    if action =='start':
        required_state = 'running'
    print("waiting to %s"%action)
    while (True):
        response = ec2.describe_instance_status(InstanceIds=[instance],IncludeAllInstances=True)
        instance_status = response['InstanceStatuses'][0]['InstanceState']['Name']
        if instance_status==required_state:
            break
        else:
            time.sleep(1)
    print()
    print("instance %s completed"%action)
    
            



action = sys.argv[1]

if __name__ == '__main__':
    #my_region = boto.ec2.connect_to_region(config['ec2']['region'])
    #reservations = my_region.get_all_instances()
    response = ec2.describe_instance_status(InstanceIds=[instance],IncludeAllInstances=True)
    print(response['InstanceStatuses'][0]['InstanceState']['Name'])
    instance_status = response['InstanceStatuses'][0]['InstanceState']['Name']
    if action == 'stop':
        if instance_status=='stopped':
            print("your instance is already stopped")
            exit(0)
        else:
            stop_instances(instance)
    if action == 'start':
        if instance_status=='running':
            print("your instance is already started")
            #exit(0)
        else:
            start_instances(instance)
            wait_for_action_completion(instance)
    if action == 'start':
        response = ec2.describe_instances(InstanceIds=[instance],)
        print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
        public_ip=response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print("connect to ec2 instance with below command")
        print("ssh -i  my_ssh_key ec2-user@%s"%public_ip)
    
