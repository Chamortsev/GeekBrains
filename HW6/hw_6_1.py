from requests import get

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

data = get(url).text

with open('nginx_logs.txt', 'w') as f:
    f.writelines(data)
result = []

with open('nginx_logs.txt', 'r') as f:
    line = f.readline()
    while line:
        content = line.split()
        remote_address = content[0]
        request_type = content[5].strip()[1:]
        requested_resource = content[6]
        result.append((remote_address, request_type, requested_resource))
        line = f.readline()

print(result)
