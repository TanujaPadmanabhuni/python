import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import json
urllib3.disable_warnings()
url = 'https://spiraplan.alticeusa.com/rest/v1/projects/90/test-cases/2173123'
username = 'administrator'
api_key = 'BE48884A-F808-4F93-8D66-07C8A42A8973'
headers = {
    'accept': 'application/json',
}
params = {
    'username': username,
    'api_key': api_key
}

response = requests.get(url, headers=headers,params=params,verify=False)
print(f"HTTP Status Code: {response.status_code}")
print(f"Response Content-Type: {response.headers['Content-Type']}")
if response.status_code == 200:
    print("API is accessible!, response data:")
    """print(json.dumps(response.json(), indent=4))"""
    if response.headers.get('Content-Type') == 'application/json':
        try:
            data = {"key": "value"}
            print(json.dumps(data, indent=4))
        except ValueError:
            pass
    else:
        print("response is not in JSON format.")
        print(response.text)
else:
    print(f'failed to access API. Status code: {response.status_code}')
    print('Error:', response.text)