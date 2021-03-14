import re

result = []
# Проблема с IPV6 Не понимаю пока как обойти это проблему.
with open('nginx_logs.txt', 'r') as f:
    line = f.readline()
    line = str(line)
    remote_addr = re.compile(r'([0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3})')
    request_datetime = re.compile(r'(\d{2}\/\w{3}\/\d{4}\:\d{2}\:\d{2}\:\d{2}\W\+\d{4})')
    request_type = re.compile(r'GET(\w*)|HEAD(\w*)')
    requested_resource = re.compile(r'(\s\/\w*\/\w*)')
    response_code = re.compile(r'(?<=["\s])(\d{3})')
    response_size = re.compile(r'(?<="\s\d{3}\s)(\d*)')

    while line:
        print(remote_addr.search(line).group(),
              request_datetime.search(line).group(),
              request_type.search(line).group(),
              requested_resource.search(line).group(),
              response_code.search(line).group(),
              response_size.search(line).group())
        line = f.readline()
