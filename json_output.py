import requests, urllib.request, json

def json_output_with_requests(url):
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    jsn = json.loads(response.text.encode('utf-8'))

    return jsn

def json_output_with_urllib(url):
    data = urllib.request.urlopen(url).read()
    jsn = json.loads(data)
    return jsn 

