import os
import requests
import sys


if len(sys.argv) < 2:
    print("Usage: get.py url <output_path>")
    exit(1)

proxy_url = os.getenv('PROXY_URL', 'http://localhost:5001')
request_url = sys.argv[1]
output_path = sys.argv[2] if len(sys.argv) == 3 else request_url

full_url = f'{proxy_url}/{request_url}'
print(f'Requesting {full_url}')
first_flag = True
with requests.get(full_url, stream=True) as r:
    r.raise_for_status()
    with open(output_path, 'wb') as outFile:
        for chunk in r.iter_content(chunk_size=8192):
            if first_flag:
                outFile.write(chunk[2:])
                first_flag = False
            else:
                outFile.write(chunk)
