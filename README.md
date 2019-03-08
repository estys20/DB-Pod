# drinkinBrosPodcastASK (Unpublished)

## Description
Drinkin' Bros. Podcast skill for Amazon Alexa. Allows for the user  to get basic information such as if a new episode has come out recently or specific episode descriptions. This skill is unpublished; however, it has been tested through the Alexa Skills Developer Console. 

The skill is based on using the requests library and an RSS feed parser to get information from the [Drinkin' Bros libsyn podcast page](https://drinkingbros.libsyn.com). ([RSS page](https://drinkingbros.libsyn.com/rss)).

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
