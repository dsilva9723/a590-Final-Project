"""Call a public API
http://text-processing.com/api/sentiment/
"""
import requests, os, json
# doc: https://docs.python-requests.org/en/latest/

"""1.create a session
"""
headers = {'Content-type':"application/json"}   #,'apikey': key
session = requests.Session()
session.headers.update(headers)

"""2.make key-value pairs for post parameter(s)
"""
data = {
    "text": "the complexity of the scientific field of machine learning can be overwhelming"
}

"""3.send a POST request
"""
response = session.post(f'http://text-processing.com/api/sentiment/', data)

"""4.print response
"""
print(f"response: {response}") #HTTP 200 OK success status
print(f"Label: {response.json()['label']}")
print(f"Probabilities: {response.json()['probability']}")
print(f"Probability of positive: {response.json()['probability']['pos']}")

"""5. json dump
"""
dir = "report" 
os.makedirs(dir, exist_ok=True)
prefix, num = "api_response_", 1
fpath = os.path.join(dir, f'{prefix}{num}.json')
with open(fpath, 'w', encoding='utf-8') as f: 
    json.dump(response.json(), f, sort_keys=False, indent=4, ensure_ascii=False)   
