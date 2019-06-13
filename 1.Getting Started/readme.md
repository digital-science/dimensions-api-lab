# Getting Started

In order to use the DimCli library it is suggested to store your Dimensions API credentials to a local file, so that you don't have to enter them every time. 

There are two ways to achieve this.

## a) using the command line tool (recommended)

Open up a terminal window from within Jupyter (New => Terminal, from the main Jupyter startup page). 

Then type in `dimcli --init`. 

A dialogue will ask you for your username and password, which is then stored in your home folder. 

DimCli will be able to retrieve this data from any notebook running on this environment. 

## b) using a local credentials file

Open the `dsl.ini.sample` file in this folder and update it as follows:

* change the username / password settings as per your credentials 
* save the file
* rename the file to `dsl.ini`

All the notebooks in this folder will automatically load the credentials from this file. 

NOTE since this method is folder-specific, if you have many files across different folders using DimCli, it is recommended to use method (a) above. 