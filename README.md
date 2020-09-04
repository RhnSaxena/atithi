# atithi

## Overview
Fusing the power of Whatsapp platform with MindMeld AI with the current tourism industry to boost tourism in India. 

## Getting Started

### Authoriztion Keys and Credentials

The projects uses many API's to perform different tasks. Proper credentials must be entered beforehand.

#### AWS Credentials (For S3 Bucket)
Enter the valid key values in itinerary/config.py
#### Cloudinary Credentials 
Enter the valid key values in itinerary/config.py

#### Twilio Credentials
Enter the valid key values in main.sh


### Installation

Use Linux as the development environment.
Clone the repository and follow these steps.

Install Docker

Create a Virtual Environment and activate it.
````
virtualenv -p python3 .
source bin/activate
````
Install dependencies
````
pip install mindmeld
pip install mindmeld[bot]
pip install -r requirements.txt
````
Pull docker images and start container
```
sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:6.7.0
sudo docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.7.0
```
or
```
docker pull mindmeldworkbench/duckling:master
docker run -p 0.0.0.0:7151:7151 mindmeldworkbench/duckling:master -ti -d
```
start num-parse
```
mindmeld num-parse --start
```
Run SH file
````
run ./main.sh
````

