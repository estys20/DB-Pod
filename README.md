# drinkinBrosPodcastASK (Unpublished)

## Description
Drinkin' Bros. Podcast skill for Amazon Alexa. Allows for the user  to get basic information such as if a new episode has come out recently or specific episode descriptions. This skill is unpublished; however, it has been tested through the Alexa Skills Developer Console. 

The skill is based on using [Flask-ASK](https://flask-ask.readthedocs.io/en/latest/) [Github](https://github.com/johnwheeler/flask-ask) with the Requests library and an RSS feed parser to get information from the [Drinkin' Bros libsyn podcast page](https://drinkingbros.libsyn.com). ([RSS page](https://drinkingbros.libsyn.com/rss)). 

Also, Speech Synthesis Markup Language (SSML) is used for some of the responses to change the way Alexa responds to user requests since the Drinkin' Bros name and some content contains abbreviated language.

## Features
* Info about newest episode: 
  - Description
  - Date & time it was published (UTC)
* Info about specific episode:
  - Description
  - Date & time it was published (UTC)

## How to Use
Create a Python virtual enviroment (this should always be done for any Python project you work on really) and activate it.
As of Python3.5 it is recommended to use [venv](https://docs.python.org/3/library/venv.html).

```
$python3 -m venv venv
source venv/bin/activate
```

Next, we can install the dependencies using the ```requirements.txt``` file.

```
$pip3 install -r requirements.txt
```

After that, run the python file and you'll see it being served locally.

```
$python3 alexa.py
```

You can use [ngrok](https://ngrok.com/) to test the Alexa Skill in the Developer Console while still continuing local development. More information for configuring the Amazon Skill Developer Console and ngrok for testing can be found [here](https://pythonprogramming.net/testing-deploying-alexa-skill-flask-ask-python-tutorial/).

## Note
The reason for this skill going unpublished is because of permissions errors. I developed this skill on macOS; however, when attempting to upload to AWS Lambda, I received errors with a cryptography package (packages have to be zipped up with the run files for Python deployments to AWS Lambda). Specifically, the cryptography package must be installed on Linux OS before being uploaded to AWS Lambda as that is what their containers use.

After using Docker to do install on an [AWS Lambda image](https://medium.com/@gotraveltoworld/use-docker-to-develop-the-aws-lambda-python-3-6-525007907369), I received errors relating to file permissions. I spent hours pouring articles and posts on how to fix this. I tried to ```chmod 777``` every file and directory and still no luck.

Proceed at your own risk when developing for AWS Lambda with Python. My recommendation is to use a Docker container. Additionally, preparing your application for deployment is different with Python than with Node.js. 

EDIT: I recommend reading [this](https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/). It wasn't out while I was developing this application, but its likely that this is the instruction I was missing. Best of luck.
