# Getting Started

You need to have valid credentials for the Dimensions Analytics API. 

These have to be stored in a file called `dsl.ini`, which should be located in this folder. 

## The credentials file 

Open the `dsl.ini.sample` file in this folder and update it as follows:

* change the username / password settings as per your credentials 
* save the file
* rename the file to `dsl.ini`

All the notebooks in this folder will automatically discover the file and load your credentials from it. 

> note: if the `dsl.ini` file is placed at the top level of your directory structure, it will be discoverable by all notebooks in sub-directories too! 

### More info

https://github.com/digital-science/dimcli#authentication
