# Cloud Pirate
![JSON](https://img.shields.io/badge/Python-JSON-yellow)
![JSON](https://img.shields.io/badge/Python-boto3-blue)

> This service gathers both the pricing information description and machine types associated with Azure and AWS cloud services. With this tool you'll be able to set the pricing information as it relates to the selected host region. You will also be able to determine the SKU Of the associated server, a description and the instance/VM type.

<hr>



### Libraries
For this project you will need 3 python libraries: JSON, Requests, and boto3.


Let’s begin by installing the requests library. To do so, run the following command:
```bash
$ pip install requests
```
If you prefer to use Pipenv for managing Python packages, you can run the following:
```bash
$ pipenv install requests
```
If you are running a non Unix environment such as windows you can use chocolatey to install pip with the following command, then run the above commands.
```bash
choco install pip
```

Next we will install the AWS SDK for python known as boto3 with pip:
```bash
pip install boto3
```

### AWS Console 

First you'll need to install AWS-CLI To be able to interact with the user console. \
To do this look at the documentation found at: [AWS-CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

After inputting your credentialed key's you will be ready to run the program.

## Running



