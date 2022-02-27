# scrape WCL, get deaths or whatever
import numpy as np
import requests #for requesting info from a url
import json

# get API keys 
keys=np.genfromtxt('keys.txt',dtype=str)

public_key=keys[0]
secret_key=keys[1]

url='https://www.warcraftlogs.com/oauth/token'
params={
	"grant_type":"client_credentials"
}

auth=(public_key,secret_key)
r=requests.post(url,data=params,auth=auth)

access_token=r.json()['access_token']

url_client='https://www.warcraftlogs.com/api/v2/client'
headers={
	"Authorization":access_token
}
params={
	"characterData="
}
r2=requests.get(url_client,headers=headers)
print(r2)
