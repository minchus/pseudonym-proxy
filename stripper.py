import sys

if len(sys.argv) != 3:
    print("Usage: stripper.py input_path bytes_to_skip output_path")

with open(sys.argv[1], 'rb') as inFile:
    inFile.seek(int(sys.argv[2]))
    with open(sys.argv[3], 'wb') as outFile:
        for chunk in iter(lambda: inFile.read(16384), b''):
            outFile.write(chunk)
