# my_tools
scripts i use while working on open source  projects

make sure you have configured aws using `aws configure`
fill parameters in ec2_devinstance.conf

1)to start ec2 instance

`python3  ec2_devinstance.py start`

2)stop ec2 instance 

`python3  ec2_devinstance.py stop`

3)create alisa for these commands in ~/.bashrc so that we dont have type full command

    `alias ec2="python3 /home/nitish/workspace/my_tools/ec2_devinstance.py"`


    now you can start or stop you instance with below command

    `ec2 start/stop`