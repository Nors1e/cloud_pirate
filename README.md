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

Begin by selecting  your pricing zone
```
Choose your pricing zone: 
```

Next choose your use case.
```
What will be your use case for this VM?
```
Finally choose your display output of how many servers you wish to view.
```
how many servers would you like to see?
```


Example output should be something like:
```
how many servers would you like to see?3

 **** Azure ****
DZH318Z0CF0K/00CN {'USD': 0.015, 'description': 'Virtual Machines DCSv2 Series', 'type': 'DCSv2'}
DZH318Z0BQ4S/00V7 {'USD': 0.01617, 'description': 'Virtual Machines DS Series', 'type': 'DS'}
DZH318Z0D1L2/016B {'USD': 0.019786, 'description': 'Virtual Machines Ddv4 Series', 'type': 'Ddv4'}

 **** AWS ****
26DJXY32K2MHJUKY {'USD': '0.0162000000', 'description': '$0.0162 per On Demand Windows t2.micro Instance Hour', 'type': 't2.micro'}
23T3HGNEQ38MPHFH {'USD': '0.0736000000', 'description': '$0.0736 per Windows t3.xlarge Dedicated Host Instance hour', 'type': 't3.xlarge'}
237AFV9YP5TV7FNC {'USD': '0.0920000000', 'description': '$0.092 per Windows z1d.large Dedicated Host Instance hour', 'type': 'z1d.large'}
```

### Applications
There are many use cases for this project, with the above code we are now able to compare and contrast AWS with Azure services. Potential future directions could be expanding to include a UI, adding additional functionality including creating and destroying server instances. 
