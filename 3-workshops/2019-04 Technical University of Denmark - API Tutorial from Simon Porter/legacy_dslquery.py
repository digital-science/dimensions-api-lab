import requests
import json
import time
import csv
from collections import Counter
import configparser

Config = configparser.ConfigParser()

Config.read("DSL.properties")


#print ("the sections are")
#print (Config.sections())


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            #if dict1[option] == -1:
                #print ("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


dimensionsUserName = ConfigSectionMap("Dimensions")['dimensionsusername']
dimensionsPassword = ConfigSectionMap("Dimensions")['dimensionspassword']



auth_data = {
  'username': dimensionsUserName,
  'password': dimensionsPassword
}

url = 'https://app.dimensions.ai'

global headers 

api_url = url + '/api'

def renewtoken():
    global headers
    auth_result = requests.post(api_url + '/auth.json', json=auth_data)
    #print(auth_result.text)
    access_token = auth_result.json()['token']
    headers = {
        'Authorization': 'JWT {}'.format(access_token)
    }
    return headers

renewtoken()

def dslquery(data, retries=0):
    start_time = time.time()
    jsonresult={}
    result = requests.post(api_url + '/dsl.json', headers=headers,data=data.encode())
    try:
        jsonresult =json.loads(result.text)
    except:
        if retries < 1:
            retries = retries + 1
            renewtoken()
            jsonresult = dslquery(data, retries)
        else:
            jsonresult = {"error":result.text}
            print (jsonresult)
    print('Execution time: {}'.format(time.time() - start_time)) 
    # The Dimensions API is limited to 1 query every 30 seconds
    time.sleep(max([0,2-(time.time() - start_time)]))
    return jsonresult




