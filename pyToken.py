import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

USERNAME = input('Please enter your username: ')
PASSWORD = getpass('Please enter your password: ')

BASEURL = 'https://sandboxdnac.cisco.com'
genToken = '/dna/system/api/v1/auth/token'

payload = {}
headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/json'
}

dnaAuth = BASEURL + genToken

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=headers, data=payload)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print('The token is :\n' + TOKEN)
