

#
# Install AWS cli
#
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
# https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html#install-macosos-bundled-sudo
```
https://docs.aws.amazon.com/zh_tw/general/latest/gr/aws-sec-cred-types.html
以 AWS 管理主控台 登入 根使用者。如需詳細資訊,請前往 Sign in as the 根使用者 in as the in the in the IAM 使用者指南 in an 。

在右上方的導覽列中,選擇帳號名稱或號碼,然後選擇 My Security Credentials (我的安全登入資料)。

展開 Access keys (access key ID and secret access key) (存取金鑰 (存取金鑰 ID 和私密存取金鑰)) 區段。

選擇Create New Access Key (建立新的存取金鑰)。如果您已經有兩個存取金鑰,則此按鈕會停用。

出現提示時,請選擇 Show Access Key (顯示存取金鑰) 或 Download Key File (下載金鑰檔案)。這是您儲存私密存取金鑰的唯一機會。

將私密存取金鑰儲存在安全位置之後,請選擇 Close (關閉)。
```
# setup aws config
LauChius-MacBook-Pro:Question1 lauchiulam$ aws configure
AWS Access Key ID [None]: AKIAJLBTM2PAGOS2OCAQ
AWS Secret Access Key [None]: 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
Default region name [None]: ap-east-1
Default output format [None]:

#https://docs.aws.amazon.com/cli/latest/reference/configure/list.html
# list aws config
LauChius-MacBook-Pro:Question1 lauchiulam$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************OCAQ shared-credentials-file
secret_key     ****************0BjN shared-credentials-file
    region                ap-east-1      config-file    ~/.aws/config
LauChius-MacBook-Pro:Question1 lauchiulam$


# ssh connect

LauChius-MacBook-Pro:Question2 lauchiulam$ chmod 400 ec2-keypair.pem
LauChius-MacBook-Pro:Question2 lauchiulam$ ssh -i /Users/lauchiulam/Project/5848cf8a7dd2-wahaha/Question2/ec2-keypair.pem ec2-user@ec2-3-129-44-130.us-east-2.compute.amazonaws.com
The authenticity of host 'ec2-3-129-44-130.us-east-2.compute.amazonaws.com (3.129.44.130)' can't be established.
ECDSA key fingerprint is SHA256:J2LEcPjsCGp+yJgfXfdi6Sku7l3eJ65K/yPFedo7EGc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
LauChius-MacBook-Pro:Question2 lauchiulam$ ssh -i /Users/lauchiulam/Project/5848cf8a7dd2-wahaha/Question2/ec2-keypair.pem ec2-user@ec2-3-129-44-130.us-east-2.compute.amazonaws.com

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
7 package(s) needed for security, out of 19 available
Run "sudo yum update" to apply all updates.




###


docker build -t shorturl .

docker tag shorturl:latest 822465260291.dkr.ecr.us-east-2.amazonaws.com/shorturl:latest

docker push 822465260291.dkr.ecr.us-east-2.amazonaws.com/shorturl:latest