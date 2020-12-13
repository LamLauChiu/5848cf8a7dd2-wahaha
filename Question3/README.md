# Notes:
Create a sample docker python flask hello-world webapp

source:

https://doedotdev.medium.com/docker-flask-a-simple-tutorial-bbcb2f4110b5


1. Setup on macOS or Linux:
- Creating a virtual environment:  \
```python3 -m venv virtualEnvironment```
- Activating a virtual environment: \
```source virtualEnvironment/bin/activate```
- Install the lists of requirements: \
```pip install -r requirements.txt```


Local run app:

```python app.py```


Build docker image:

```docker build -t short_url_app:latest .```

```docker run -d -p 5000:5000 --name short_url_app short_url_app:latest```


Create a repository in ECR
Soucre:
https://towardsdatascience.com/how-to-use-docker-to-deploy-a-dashboard-app-on-aws-8df5fb322708

1.Retrieve an authentication token and authenticate your Docker client to your registry.
Use the AWS CLI:

```aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ACCOUNT NUM>.dkr.ecr.<REGION>.amazonaws.com```

2.Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:

```docker build -t shorturl .```

3.After the build completes, tag your image so you can push the image to this repository:
```docker tag shorturl:latest <ACCOUNT NUM>.dkr.ecr.<REGION>.amazonaws.com/shorturl:latest```

4.Run the following command to push this image to your newly created AWS repository:
```docker push <ACCOUNT NUM>.dkr.ecr.<REGION>.amazonaws.com/shorturl:latest```


Sample Hello-world Flask weapp
source: https://doedotdev.medium.com/docker-flask-a-simple-tutorial-bbcb2f4110b5


Set up Jenkins
https://www.jenkins.io/download/lts/macos/

Jenkins can be installed using the Homebrew package manager. Homebrew formula: jenkins-lts This is a package supported by a third party which may be not as frequently updated as packages supported by the Jenkins project directly.

Sample commands:
```
Install the latest LTS version: brew install jenkins-lts
Install a specific LTS version: brew install jenkins-lts@YOUR_VERSION
Start the Jenkins service: brew services start jenkins-lts
Restart the Jenkins service: brew services restart jenkins-lts
Update the Jenkins version: brew upgrade jenkins-lts
```
After starting the Jenkins service, browse to http://localhost:8080 and follow the instructions to complete the installation. Also see the external materials for installation guidelines. For example, this blogpost describes the installation process.


AWS plugins for Jenkins
```
aws-credentials:1.28
pipeline-aws:1.41
```

- the aws-credentials plugin allows us to configure AWS credentials from the Jenkins credentials configuration screen

- the pipeline-aws plugin allows us to use the 
AWS credentials in a pipeline stage. We’ll use them in the stage where we call the Gradle task to deploy the CloudFormation to AWS.