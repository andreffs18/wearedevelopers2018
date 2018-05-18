# Basic Challenge

Here you can find all files that were required to complete the first challenge of Boc Group.


## Stack

We used Python (3.6) to develop the API client that makes all requests.


## Usage

To run this, you must install python 3.6 and pipeenv using **brew**

> If you don't have brew you can install it by going to their website: https://brew.sh/

```shel
$ brew install python pipeenv
```


After installing those two dependencies, run ```$ pipenv install``` to install all necessary requirements.


Now we just need to open a python shell, import the **Api Client** and initialize it with the **developer_id**:
 
```shell
$ pipenv run python 
from basic_challenge import Client
c = Client("<developers_id>")
```


## Client Methods


### Get Model Image

This method makes a GET request to the challenge URL and saves an image file. 

The default file name is **"model.jpg"** but can be changed by the optional argument **filename**


#### Usage
```python 
from basic_challenge import Client
c = Client("<developers_id>")
c.get_model_image(filename="image.jpg")
```


### Send Code Number

This method makes a ~GET~ POST request with the given code number. 


#### Usage
```python 
from basic_challenge import Client
c = Client("<developers_id>")
c.send_code_number("<code_number>")
```









