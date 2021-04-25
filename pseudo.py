import requests
import sys


if len(sys.argv) != 3:
    print("Usage: pseudo.py url output_path")
    exit(1)

first_flag = True
with requests.get(f"https://pseudonym-proxy.herokuapp.com/{sys.argv[1]}", stream=True) as r:
    r.raise_for_status()
    with open(sys.argv[2], 'wb') as outFile:
        for chunk in r.iter_content(chunk_size=8192):
            if first_flag:
                outFile.write(chunk[2:])
                first_flag = False
            else:
                outFile.write(chunk)
