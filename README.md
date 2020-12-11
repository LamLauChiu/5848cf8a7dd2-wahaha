# 5848cf8a7dd2-wahaha

#

sudo yum install git

#
Q1.​ Access​ Log​ analytics
#
1. Count​ the total​ number​ ​of HTTP​ requests​ recorded​ by​ this​ access​ logfile
2. Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to
2019-06-19​ 23:59:59,​ inclusively
3. Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​to the source​
IP)
#
prerequisite: \
Install Git :
```sudo yum install git -y```
Install 
```sudo yum install jq -y``` 

Clone Git Souce: ```git clone https://github.com/LamLauChiu/5848cf8a7dd2-wahaha.git```
#
Q1.1 Count​ the total​ number​ ​of HTTP​ requests​ recorded​ by​ this​ access​ logfile
#
Answer: \
Go to Quesiton1 Folder : ```cd 5848cf8a7dd2-wahaha/Question1/```

Run the Script: ```. Q1.1-answer.sh``` 

Output: 

![alt text](./src/images/Q1.1-screencap.png)

#
Q1.2 Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to
2019-06-19​ 23:59:59,​ inclusively
#
Answer: \

Run the Script: ```. Q1.2-answer.sh``` 

Output: 

![alt text](./src/images/Q1.2-screencap.png)

| No. of Requests Counted  | Ip Address |
| --- | --- |
| 730 | 1.222.44.52 |
| 730 | 118.24.71.239 |
| 723 | 119.29.129.76 |
| 486 | 148.251.244.137|
| 440 | 95.216.38.186 |
| 440 | 136.243.70.151 |
| 437 |213.239.216.194 |
| 436 | 5.9.71.213 |
| 436 |5.189.159.208|
| 406 | 5.9.108.254 |
#
Q1.3 Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​to the source​
IP)
#
Answer: \

Run the Script: ```. Q1.3-answer.sh``` 

Output: 

![alt text](./src/images/Q1.3-screencap.png)
| No. of Requests Counted  | Ip Address | Country |
| --- | --- | -- |
| 730 | 1.222.44.52 | KR |
| 730 | 118.24.71.239 | CN |
| 723 | 119.29.129.76 | CN |
| 486 | 148.251.244.137| DE | 
| 440 | 95.216.38.186 |  DE |
| 440 | 136.243.70.151 |  DE |
| 437 |213.239.216.194 | DE |
| 436 | 5.9.71.213 | DE |
| 436 |5.189.159.208| DE |
| 406 | 5.9.108.254 | DE |

Remark: \
DE = Deutschland \
CN = China \
KR = Korea 
#
Q2.​ AWS​ API​ programming
#
Please​ help​ to​ prepare​ a script​ to​ query​ AWS​ API​ and​ look up the public​ IP​ of the instance​ with the​ specific​ EC2​ Name​ tag.​ Then​ the script​ should​ execute​ the ssh​ command 
 
ssh​ ec2-user@EC2_PUBLIC_IP​ .
#
prerequisite: \

1. Setup on macOS or Linux:
- Creating a virtual environment:  \
```python3 -m venv virtualEnvironment```
- Activating a virtual environment: \
```source virtualEnvironment/bin/activate```
- Install the lists of requirements: \
```pip install -r requirements.txt```

2. Pepare the ec2-keypair.pem key file in put it inside "5848cf8a7dd2-wahaha/Question2/" directory

3. Create the instances in AWS and Add the Name of tag as "api-server-002"

#
Answer: \
Go to Quesiton1 Folder : ```cd 5848cf8a7dd2-wahaha/Question2/```

To test the successful case by running the Script: \
```python Q2-answer.py api-server-002``` 

Output:
![alt text](./src/images/Q2-screencap-1.png)

To test the not-exiting-host case by running the Script: \
```python Q2-answer.py not-exiting-host```

Output:
![alt text](./src/images/Q2-screencap-2.png)
#