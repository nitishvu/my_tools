# my_tools
scripts i use while working on open source  projects

### Start and Stop your ec2 dev instance without aws console


Make sure you have configured aws using `aws configure`
fill parameters in ec2_devinstance.conf.
Try to use [my_ec2_policy](https://github.com/nitishvu/my_tools/blob/master/my_ec2_policy.json) present in this repo to restrict user 
also you can add sshkey path to get exact command to ssh

1)start ec2 instance.


    `python3  ec2_devinstance.py start`
    


    o/p:
    52.66.XX.XX
    connect to ec2 instance with below command
    ssh -i  my_ssh_key ec2-user@52.66.XX.XX




2)stop ec2 instance. 

    python3  ec2_devinstance.py stop


3)create alisa for these commands in ~/.bashrc so that we dont have type full command

    alias ec2="python3 /home/nitish/workspace/my_tools/ec2_devinstance.py"


Now you can start or stop you instance with below command


        `ec2 start/stop`




