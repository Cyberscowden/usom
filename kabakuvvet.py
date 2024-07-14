import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('http://www.usom.gov.tr/url-list.txt', verify=False)
with open("usom.txt", "wb") as binary_file:
    binary_file.write(response.content)

def check(url):
    with open("usom.txt") as f:
        lines = f.read().split('\n')
        print(lines)
        for line in lines:
            if line == url:
                return f"{url} zararlıdır"
    return f"{url} zararlı değildir"

print(check('http://zararli-url.com'))
print(check('http://zararsiz-url.com'))