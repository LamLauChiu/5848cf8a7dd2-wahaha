"""
On macOS and Linux:
- Creating a virtual environment:
python3 -m venv virtualEnvironment
- Activating a virtual environment:
source virtualEnvironment/bin/activate
- Install the lists of requirements:
pip install -r requirements.txt



boto3 Tutorial Source:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

Tagging Best Practices:
https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf

Moto - Mock AWS Services:
https://github.com/spulec/moto


Troubleshoot:
AWS S3 CLI - Could not connect to the endpoint URL
https://stackoverflow.com/questions/40409683/aws-s3-cli-could-not-connect-to-the-endpoint-url

Filter instances by state with boto3
https://stackoverflow.com/questions/38122563/filter-instances-by-state-with-boto3

Connecting to your Linux instance using SSH
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html


"""

import boto3
import os
import sys


# Get Name tag value from arg
print("Name tag :{}".format(sys.argv[1]))
name_tag = sys.argv[1]
path_of_pem = 'ec2-keypair.pem'
login_user = 'ec2-user' # Default
region = 'us-east-2' # Default

def retrieve_first_instance_ip_address(ec2, name_tag):
    # tag:Name - {Name} is key under Tags
    filterValue = {'Name': 'tag:Name', 'Values': [name_tag]}
    hosts = []
    for host in ec2.instances.filter(Filters=[filterValue]):
        hosts.append(host.public_ip_address)
        #print(host.public_ip_address)

    print( "no. of instances retrieved:",len(hosts))    
    if len(hosts) == 0:
        return ''
    else:
        #print(hosts[0])
        return hosts[0]


def main():
    print("==Script Begin==")
    ec2 = boto3.resource('ec2', region)
    #print(ec2.instances)
    # for instance in ec2.instances.filter(
    #     Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'terminated']}]):
    #     print(instance.id, instance.instance_type)
    instance_ip_address = retrieve_first_instance_ip_address(ec2, name_tag)
    #print(instance_ip_address)
    if len(instance_ip_address) == 0:
        print("Host not found")
    else:
        ec2_public_ip = instance_ip_address
        print("ec2_public_ip: {}".format(ec2_public_ip))

        # AWS ssh pattern:
        # ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name
        # ssh -i ec2-keypair.pem ec2-user@ec2-3-129-44-130.us-east-2.compute.amazonaws.com

        ssh_command = "ssh -i {} {}@{}".format(path_of_pem, login_user, ec2_public_ip)
        print(ssh_command)
        os.system(ssh_command)
        print("==Script End==")



if __name__ == '__main__':
    main()