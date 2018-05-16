# Basic Challenge

Here you can find all files that were required to complete the first challenge of Boc Group.


## Stack

We used Python (3.6) to develop the API client that makes all requests.


## Usage

To run this, you must install python 3.6 and pipeenv using **brew**

> If you don't have brew you can install it by going to their website: https://brew.sh/

```shel
$ brew install python
$ brew install pipeenv
```


After installing those two dependencies, run ```$ pipenv install``` to install all necessary dependencies.


Now, we just need to open a python shell, import the **Api Client** and initialize it with the **developer_id**:
 
```shell
$ pipenv run python 
from basic_challenge import Client
c = Client("<developers_id>")
```




